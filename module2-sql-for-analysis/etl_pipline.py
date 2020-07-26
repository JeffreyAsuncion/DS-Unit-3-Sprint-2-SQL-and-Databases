#extract, transform, load

import json
import os 
from dotenv import load_dotenv
import pandas as pd 
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

load_dotenv() # looks inside the .env file for some env vars

# passes env var values to python var

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASS = os.getenv("DB_PASS", default="OOPS")

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")



############### MIKE IS GOOD IM JUST TIRED 
############### 0:23:39






class StorageService():
    pass


if __name__ == "__main__":

    serivce = StorageService()


    #
    # EXTRACT AND TRANSFORM
    #

    characters = service.get_characters()
    print(type(characters), len(characters))
    print(characters[0])


    #
    # LOAD
    #

    service.create_characters_table()

    service.insert_characters(characters)