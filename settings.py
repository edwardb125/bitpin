
from pymongo import MongoClient

client = MongoClient("mongodb+srv://erfan:1234@cluster0.ac0gyj1.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('todos')
contents = db.content