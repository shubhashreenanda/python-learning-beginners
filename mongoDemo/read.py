from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['mydb']
print('Database created')
collection = database['product']
#print(collection.find_one())
cursor = collection.find({"name": "Dell"})
print('name found')
for eac_doc in cursor:
    print(eac_doc)