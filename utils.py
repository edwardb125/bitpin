from xml.dom.minidom import Document
from settings import contents
from flask import render_template, request

user_score = {}
result = contents.find()
for i in result:
    user_score[i['title']] = -1

def home_page_function():
    return 'hello'


def list_function():
    result = contents.find()
    content = [result, user_score]
    return render_template('list.html', contents = content)
    

def article_function():
    result = contents.find()
    content = [result, user_score]
    return render_template('article.html', contents = content)


def add_vote_function():
    global user_score
    vote = request.form.get("vote")
    topic_name = request.form.get("title")
    user_score[topic_name] = int(vote)
    content = contents.find_one({
        'title': topic_name
    })
    score = ((content['score'] * content['vote']) + int(vote))/(content['vote'] + 1)
    update_object = {"$set": {}}
    update_object["$set"]['score'] = round(score, 3)
    contents.update_one({'title': topic_name}, update_object)
    return vote