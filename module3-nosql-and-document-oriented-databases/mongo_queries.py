import pymongo
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pdb import set_trace as breakpoint


load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("\n----------------")
print("URI:", connection_uri)



client = pymongo.MongoClient(connection_uri)


print("\n----------------")
print("CLIENT:", type(client), client)

print("\n")
print(client.list_database_names())

# Setting the DB to sample_analytics
db = client.sample_analytics
print(db.list_collection_names())


# Access a specific collection
customers = db.customers
print(customers.count_documents({}))


all_customers = customers.find()
import pandas as pd
df = pd.DataFrame(all_customers)
print(df.head())
print(df.shape)
print(df.columns)

customers.insert_one({'full name': 'Robert Poulson'})
print(customers.count_documents({}))

