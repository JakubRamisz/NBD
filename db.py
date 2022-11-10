from pymongo import MongoClient

client = MongoClient('mongodb://mongodb://admin:adminp@localhost:27017')
db = client['nbddb']

def get_collection(name: str):
    collection = db[name]
    return collection
    