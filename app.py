from flask import (
    Flask, request, render_template, url_for, redirect, flash, session, jsonify)
from flask.json import JSONEncoder
from datetime import timedelta
from datetime import datetime
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.agents.agent_types import AgentType
from langchain.schema import AIMessage, HumanMessage
from dotenv import load_dotenv
from nltk.tokenize import word_tokenize

import joblib
import pandas as pd
import openai
import markdown
import nltk
import os
import json
import re

app = Flask(__name__)

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY
MODEL = 'gpt-3.5-turbo-1106'
TEMPERATURE = 0.0
MAX_TOKENS = 4096  # GPT-3.5의 최대 토큰 길이임(입력, 출력 동일함)

nltk.download('punkt')  # 토크나이저에 필요한 데이터를 다운로드합니다.

# Personalized AI
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002', openai_api_key=OPENAI_API_KEY, max_retries=20)
knowledge_model = ChatOpenAI(temperature=0, model_name=MODEL)

vector_gift = Chroma(persist_directory='csv_db', embedding_function=embeddings)
qa_gift = ConversationalRetrievalChain.from_llm(knowledge_model, vector_gift.as_retriever(search_kwargs={"k": 3}), return_source_documents=True)

app.config['SESSION_COOKIE_MAX_SIZE'] = 4800  # 세션의 크기에 대한 문제
app.config['SECRET_KEY'] = 'your_secret_key_here'  # 보안을 위한 시크릿 키 설정

print('Initialization complete.')

# Basic function
# 기본 함수: context의 메시지가 최대 길이를 초과했는지 확인하는 코드
def check_tokens(items):
    cnt = 0

    if items is None:
        return cnt

    for item in items:
        cnt += len(item['content'])

    return cnt

# 기본 함수: QA Model에서의 질의 응답에 대한 History 관리
def manage_history(lists):    
    tot_size = 0
    if len(lists) >= 1:
        for item in lists:
            tot_size += len(item['content'])

        if tot_size >= 3000:
            lists = lists[2:]
        
        # Human / AI 메시지 형태로 변환
        results = []
        for item in lists:
            if item['type'] == 'human':
                results.append(HumanMessage(content=item['content'], additional_kwargs=item['additional_kwargs'], example=item['example']))
            else:
                results.append(AIMessage(content=item['content'], additional_kwargs=item['additional_kwargs'], example=item['example'])) 
            
        return results
    else:
        return lists
        
# 기본 함수: 응답이 오면 해답 메시지와 출처 메시지를 구분한다.
def questioning(model, lists, query):
    results = manage_history(lists)  # manage_history 함수가 리스트를 반환하도록 수정 필요
    result = model({"question": query, "chat_history": results})
    print(result['answer']) # 응답 출력
    refs = []
    print('Reference:')
    for item in result['source_documents']:
        filename_with_extension = os.path.basename(item.metadata['source'])
        filename = os.path.splitext(filename_with_extension)[0]
        print(filename)
        refs.append(filename)
    
    #lists.append(HumanMessage(content=query, additional_kwargs={}, example=False))
    #lists.append(AIMessage(content=result['answer'], additional_kwargs={'source':refs}, example=False)) 
    
    print(refs)
    
    lists.append({'type':'human', 'content':query, 'additional_kwargs':{}, 'example':False})
    lists.append({'type':'ai', 'content':result['answer'], 'additional_kwargs':{'source':refs}, 'example':False})
            
    return lists


@app.route('/')
def hello():
    return 'Hello, Welcome to My World!'


@app.route('/retrieveai', methods=['GET', 'POST'])
def retrieveai():
    if request.method == 'GET':
        sel_lang = request.args.get('lang')
        print(sel_lang)

        if (sel_lang is not None):
            session['lang'] = sel_lang
            
        return render_template('retrieveai.html', lang=session.get('lang', ''))
    else:
        message = request.form.get('text')
        print(message)
        chat_history = session.get('gift_history', [])
        print(chat_history)
        chat_history = questioning(qa_gift, chat_history, message)
        answer = chat_history[-1]['content']
        result = markdown.markdown(answer, extensions=['md_in_html'])
        session['gift_history'] = chat_history
        
        return jsonify({'data':result})


if __name__ == '__main__':
    session['lang'] = 'ko'
    session['gift_history'] = []
    app.run()