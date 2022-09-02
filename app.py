from flask import Flask, redirect, request
from utils import list_function, add_vote_function, init
from settings import contents
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def list():
    content = list_function(contents)
    return render_template('list.html', contents = content)

@app.route('/vote', methods=['GET'])
def article():
    content = list_function(contents)
    return render_template('article.html', contents = content)
    

@app.route('/add_vote', methods=['POST'])
def add_vote():
    add_vote_function(contents, request)
    return redirect('/')
 

if __name__ == '__main__':
    init(contents)
    app.run(port=5000, debug= True)