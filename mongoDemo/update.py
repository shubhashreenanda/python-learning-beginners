from re import search

from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['mydb']
print('Database created')
collection = database['product']
filter1 = {"name": "Dell"}
collection.update_one(filter1, {"$set": {"price":18000}})