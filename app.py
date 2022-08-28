from flask import Flask, redirect
from utils import list_function, article_function, add_vote_function, init

app = Flask(__name__)

@app.route('/', methods=['GET'])
def list():
    return list_function()

@app.route('/vote', methods=['GET'])
def article():
    return article_function()

@app.route('/add_vote', methods=['POST'])
def add_vote():
    add_vote_function()
    return redirect('/')
 

if __name__ == '__main__':
    init()
    app.run(port=5000, debug= True)