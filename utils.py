user_score = {}


def init(content_collection):
    result = content_collection.find()
    for i in result:
        user_score[i['title']] = -1 #-1 means: No points have been given
    return user_score


def list_function(content_collection):
    result = content_collection.find()
    content = [result, user_score]
    return content


def update_vote(content_collection, topic_name, vote):
    vote_number = vote
    score = 0
    add_user_count = True
    content = content_collection.find_one({
        'title': topic_name
    })
    if(user_score[topic_name] != -1):
        vote_number = vote_number - user_score[topic_name]
        add_user_count = False
    user_score[topic_name] = vote
    
    update_object = {"$set": {}}
    if add_user_count == True:
        update_object["$set"]['vote'] = content['vote'] + 1
        score = ((content['score'] * content['vote']) + vote_number)/(content['vote'] + 1)
    else: 
        score = ((content['score'] * content['vote']) + vote_number)/(content['vote'])
    update_object["$set"]['score'] = round(score, 3)
    updated = content_collection.update_one({'title': topic_name}, update_object)
    return updated


def add_vote_function(content_collection, request):
    vote = request.form.get("vote")
    topic_name = request.form.get("title")
    updated = update_vote(content_collection, topic_name, int(vote))
    return updated