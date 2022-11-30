from pymongo import MongoClient

# try 'mongodb://localhost:27017' if authentication fails
client = MongoClient('mongodb://admin:adminp@localhost:27017')
db = client['nbddb']

def get_collection(name: str):
    collection = db[name]
    return collection
    