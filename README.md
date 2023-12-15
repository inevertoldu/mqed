# How to use python and LLM(ChatGPT) in educational settings

<h3>1. Get your own ChatGPT API Key</h3>
If you would like to get your own API key, follow the link <a href="https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/">click</a>
<h3>2. Install virtual environment(anaconda)</h3>
Anaconda is a software to support virtual environment for R and Python. Once you install this programme, you don't need to install Python.<br>
follow the link <a href="https://www.anaconda.com/download/">click</a>
<h3>3. create and activate virtual environment</h3>
Open up your terminal (or command window) and type this command:<br>
<b>conda create -n mqed python=3.11</b><br>
<b>conda activate mqed</b>
<b>pip install -r requirements.txt</b><br>
you can download requirements.txt from the git repository<br>
<p></p>
If you need to install any specific library, open up your terminal in the OS and type this command:<br>
<b>pip install <i>package_name</i></b>

<h3>4. Create your own environment file</h3>
In order to run codes in this repository, you have to create your own environment file.<br>
You should create '.env' file by using notepad or text editor.<br>
The path should be the same as repository files.<br><br>

FLASK_APP=app.py<br>
FLASK_ENV=development<br>
OPENAI_API_KEY=your_api_key_here<br>
UPLOAD_FOLDER = './uploads'<br>
export FLASK_APP=app.py<br>
export FLASK_DEBUG=true<br><br>

