import os
from dotenv import load_dotenv
import psycopg2

# Purge the virtualenv by pipenv --rm
# Install binary version: pipenv install psycopg2-binary

load_dotenv() #> loads contents of the .env file into the script's environment


DB_NAME = os.getenv(DB_NAME)
DB_USER = os.getenv(DB_USER)
DB_PASS = os.getenv(DB_PASS)
DB_HOST = os.getenv(DB_HOST)

print(DB_NAME, DB_USER, DB_PASS, DB_HOST)

exit()

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, 
                        user=DB_USER,
                        password=DB_PASS, 
                        host=DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries
cursor = conn.cursor()

### An example query
cursor.execute('SELECT * from test_table;')

### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cursor.fetchall()
print(results)