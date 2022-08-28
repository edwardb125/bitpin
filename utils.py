from xml.dom.minidom import Document
from settings import contents
from flask import render_template, request

user_score = {}
result = contents.find()
for i in result:
    user_score[i['title']] = -1 #-1 means: No points have been given

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


def update_vote(topic_name, vote):
    vote_number = vote
    add_user_count = True
    content = contents.find_one({
        'title': topic_name
    })
    if(user_score[topic_name] != -1):
        vote_number = vote_number - user_score[topic_name]
        add_user_count = False
    user_score[topic_name] = vote
    score = ((content['score'] * content['vote']) + vote_number)/(content['vote'] + 1)
    update_object = {"$set": {}}
    if add_user_count == True:
        update_object["$set"]['vote'] = content['vote'] + 1
    update_object["$set"]['score'] = round(score, 3)
    contents.update_one({'title': topic_name}, update_object)
    


def add_vote_function():
    print('in here')
    vote = request.form.get("vote")
    topic_name = request.form.get("title")
    update_vote(topic_name, int(vote))
    return vote