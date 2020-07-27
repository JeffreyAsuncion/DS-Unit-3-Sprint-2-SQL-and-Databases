# app/mongo_queries.py
import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)
'''
FYI: if you see "pymongo.errors.ServerSelectionTimeoutError [SSL: CERTIFICATE_VERIFY_FAILED]",
 and you have already allowed access from all IP addresses, and you have already 
 installed the dnspython package, try adding &ssl=true&ssl_cert_reqs=CERT_NONE 
 to the end of the connection string (thanks to Aaron from DS 14)!
'''


client = MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
print("DATABASES:", client.list_database_names())

# breakpoint()
# client; dir(client)
# from pprint import pprint; pprint(dir(client))
# client.list_database_names()


# create new instance in MONGO client.my_test_database
# similiar we could use db = client['my-test-database']
db = client.my_test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)
print("COLLECTIONS:", db.list_collection_names())


collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)
print("DOCUMENT COUNT:", collection.count_documents({})) # needs filter of empty dict {}
# insert and find methods using breakpoint(), pprint(dir(collectoions))
print("COLLECTION LIST:",db.list_collection_names())




collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    "parrents": ["Pikcachu A", "Raichu"],
    "other_attr": {
        "a":1,
        "b":2,
        "c": 3
    }
})

print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))
