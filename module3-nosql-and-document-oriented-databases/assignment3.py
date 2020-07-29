# Store RPG data in our MongoDB instance
import os
import sqlite3
import pandas as pd
import pymongo
from dotenv import load_dotenv
from pymongo import MongoClient
from pdb import set_trace as breakpoint

#
# Part One:  get data from 1. Sqlite or 2. Postgresql

#
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query1 = "SELECT *  FROM charactercreator_character;"
#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)
question1 = "What does the data look like?"
result1 = cursor.execute(query1).fetchall()

# # print the first record
# print(question1, result1[0])

# # print the result of the query
# print(question1, result1)

df = pd.DataFrame(result1)

# print(df.head())

#
# TODO: df.to_dict from DataFrame to JSon Format
#

dict = df.to_dict()
# print(dict)



load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("\n----------------")
print("URI:", connection_uri)



client = pymongo.MongoClient(connection_uri)

#
# TODO: db.collection.insertMany({})
#

db = client.rpg_data

rpg_data = db.rpg_data
print(rpg_data.count_documents({}))

rpg_data.insertOne({dict})