import redis
from pymongo import MongoClient
from db.config import MONGO_CONNECTION_STRING, MONGO_DB, REDIS_HOST, REDIS_PORT, REDIS_DB


redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
client = MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB]

hash_prefix = {
    'account': 'Account:',
    'transaction': 'Transaction:'
}

def get_collection(name: str):
    collection = db[name]
    return collection
    