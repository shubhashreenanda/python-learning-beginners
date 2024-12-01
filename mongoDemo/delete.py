from re import search

from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['mydb']
print('Database created')
collection = database['product']
collection.delete_one({"name": "Dell"})

cursor1 = collection.find({"name": "Dell"})
for eac_doc in cursor1:
    print(eac_doc)