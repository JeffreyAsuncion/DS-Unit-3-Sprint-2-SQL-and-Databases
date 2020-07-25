import os
import psycopg2
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import pandas as pd

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")

# sanity check if this really works
print(DB_NAME, DB_USER, DB_PASS, DB_HOST)
# exit() # to check the .env creditials were passed

# Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, 
                        user=DB_USER,
                        password=DB_PASS, 
                        host=DB_HOST)

# A "cursor", a structure to iterate over db records to perform queries
cursor = conn.cursor()


# FETCH DATA

cursor.execute('SELECT * from test_table;') # in postgreSQL cannot fetch here
results = cursor.fetchall()
# print(results)



### FROM DS 15 timestamp 1:51:13

my_dict = {"a":1, "b": ["dog", "cat", 42], "c": 'true'}
# insertion_query = "INSERT INTO test_table (name, data) VALUES (%s, %s)"
## This is object oriented approach with cursor.
# cursor.execute(insertion_query,
#     ('A rowwwwww', 'null'))

# cursor.execute(insertion_query,
#     ('Another row with a JSONNNN', json.dumps(my_dict))
# )


insertion_query = "INSERT INTO test_table (name, data) VALUES %s"
## This is functional approach using execute_values
execute_values(cursor, insertion_query, [
    ('A rowwww', 'null'),
    ('Another row, with JSOOONNNNN', json.dumps(my_dict)),
    ('Third row', '3')
]) # data must be in a list of tuples!!!!!







################## Connect to SQLite3 db for RPG data ###################


import sqlite3

sl_conn = sqlite3.connect("rpg_db.sqlite3")
sl_cursor = sl_conn.cursor()
characters = sl_cursor.execute("SELECT * FROM charactercreator_character;").fetchall()
print(characters)


################## Create Character Table in PostGRES ###################


create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	level INT,
	exp INT,
	hp INT,
	strength INT,
	intelligence INT,
	dexterity INT,
	wisdom INT
)
''' 

cursor.execute(create_character_table_query)
conn.commit()



################## Insert Character Data in PostGRES ###################
# INSERT DATA

for character in characters:

    insert_query = f'''INSERT INTO rpg_characters 
    (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES {character}
    '''
    # test it first in print()
    # print(insert_query)
    #then use cursor
    cursor.execute(insert_query)



# ACTUALLY SAVES TRANSACTIONS
conn.commit() # commits to DB
