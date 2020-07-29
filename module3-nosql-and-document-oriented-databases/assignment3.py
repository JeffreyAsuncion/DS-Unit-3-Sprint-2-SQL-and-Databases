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

query = "SELECT *  FROM charactercreator_character;"
results = cursor.execute(query).fetchall()
# print("RESULT", results) #> returns cursor object w/o results (need to fetch the results)
# print("type:", type(results))

#
# Prepare df 
#

columns = ['character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']
rpg_df = pd.DataFrame(results, columns=columns)
print(rpg_df.head())


#
# TODO: result to dict
#

rpg_dict = rpg_df.to_dict('records')


#
# TODO: create and insert to mongoDB
#

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

db = client.rpg_database 

collection = db.charactercreator_character

collection.insert_many(rpg_dict)