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

# This finds the rpg_db.sqlite3 in module1-introduction-to-sql
# What is the filepath to connect to our sqlite database?
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "rpg_db.sqlite3")


# approach one class per database

class SQLiteService():
    def __init__(self, db_filepath=DB_FILEPATH):
        self.connection = sqlite3.connect(DB_FILEPATH)
        self.cursor = self.connection.cursor()

    def fetch_characters(self):
        return self.cursor.execute("SELECT * FROM charactercreator_character;").fetchall()


# class ElephantSQLService():
#     pass




class StorageService():
    def __init__(self):
        self.sqlite_connection = sqlite_service.connect(DB_FILEPATH)
        self.sqlite_cursor = self.sqlite_connection.cursor()
        self.pg_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        self.pg_cursor = self.pg_connection.cursor()

    def fetch_characters(self):
        return self.sqlite_connection.execute("SELECT * FROM charactercreator_character;").fetchall()

    def create_character_table(self):
        create_query = """
        DROP TABLE IF EXISTS characters; -- allows this to be run idempotently, avoids psycopg2.error
        CREATE TABLE IF NOT EXISTS characters (
            character_id SERIAL PRIMARY KEY,
            name VARCHAR(30)
            level INT,
            exp INT,
            hp INT,
            strength INT,
            intelligence INT,
            dexterity INT,
            widsom INT
        );
        """





if __name__ == "__main__":

    #
    # EXTRACT AND TRANSFORM
    #

    sqlite_service = SQLiteService()

    characters = sqlite_service.fetch_characters()
    print(type(characters), len(characters))
    print(characters[0])

    exit()

    #
    # LOAD
    #

    # pg_service = ElephantSQLService()

    # pg_service.create_characters_table()

    # pg_service.insert_characters(characters)




    # characters = service.get_characters()
    # print(type(characters), len(characters))
    # print(characters[0])



    service.create_characters_table()

    service.insert_characters(characters)