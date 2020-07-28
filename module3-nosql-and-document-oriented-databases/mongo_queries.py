import pymongo
import os
from dotenv import load_dotenv
from pymongo import MongoClient



load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)



client = pymongo.MongoClient(connection_uri)
exit()

print("----------------")
print("CLIENT:", type(client), client)


print(client.list_database_names())



# im connecting to the DS15 database