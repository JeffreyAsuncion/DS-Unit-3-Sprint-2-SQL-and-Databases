import os
import psycopg2
from dotenv import load_dotenv

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

# An example query
cursor.execute('SELECT * from test_table;') # in postgreSQL cannot fetch here

# Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cursor.fetchall()
print(results)