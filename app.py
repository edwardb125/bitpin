from flask import Flask, redirect
from utils import home_page_function, list_function, article_function, add_vote_function

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
    app.run(port=5000, debug= True)