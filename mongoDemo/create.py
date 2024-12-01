from itertools import product

from pymongo import MongoClient

client = MongoClient('localhost',27017)
database = client['mydb']
print('Database created')
collection = database['product']
print('Collection created')
products = {
    "name": "Dell",
    "price": 10000,
},{
    "name": "HP",
    "price": 1200,
},{
    "name": "Mac",
    "price": 200000,
}
result = collection.insert_many(products)
print(result.inserted_ids)