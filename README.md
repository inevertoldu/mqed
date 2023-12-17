# How to use python and LLM(ChatGPT) in educational settings

<h3>1. Install virtual environment(anaconda)</h3>
Anaconda is a software to support virtual environment for R and Python. Once you install this programme, you don't need to install Python.<br>
follow the link <a href="https://www.anaconda.com/download/">click</a>
If you successfully install 'Anaconda' on your computer, you have to create a virtual environment by using command window or terminal.<br>
Just input following codes.<br><br>
<b>conda create -n mqed python=3.11</b><br>
<b>conda activate mqed</b>

<h3>2. Down this repository files to your computer.</h3>
By clicking 'Download Zip' in the menu <b>[<> Code]</b>, you can download them.<br>
Then, unzip the files in your local device.<br>
There is "requirements.txt" to install libraries you need to use.<br>
Please input following codes:<br><br>
  
<b>pip install -r requirements.txt</b><br>

<p>Please visit <a href='https://pip.pypa.io/en/stable/installation/'>this page</a> if you want to install pip on your OS</p>

If you need to install any specific library, open up your terminal in the OS and type this command:<br><br>
<b>pip install <i>package_name</i></b>

<h3>3. Get your own ChatGPT API Key</h3>
If you would like to get your own API key, follow the link <a href="https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/">click</a>

<h3>4. Create your own environment file</h3>
In order to run codes in this repository, you have to create your own environment file.<br>
You should create '.env' file by using notepad or text editor.<br>
The path should be the same as repository files.<br><br>

<i>
FLASK_APP=app.py<br>
FLASK_ENV=development<br>
OPENAI_API_KEY=your_api_key_here<br>
UPLOAD_FOLDER = './uploads'<br>
export FLASK_APP=app.py<br>
export FLASK_DEBUG=true<br><br>
</i>

