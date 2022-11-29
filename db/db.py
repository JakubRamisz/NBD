import os
from pymongo import MongoClient
from db.config import MONGO_CONNECTION_STRING, MONGO_DB, REDIS_CONNECTION_STRING


# try 'mongodb://localhost:27017' if authentication fails

os.environ['REDIS_OM_URL'] = REDIS_CONNECTION_STRING
client = MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB]

def get_collection(name: str):
    collection = db[name]
    return collection
    