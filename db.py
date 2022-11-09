from pymongo import MongoClient

client = MongoClient('mongodb://admin:adminp@localhost:27017')
db = client['nbddb']
collection = db['test_collection']
collection.insert_one({'title': 'test'})
print(collection.find_one())
