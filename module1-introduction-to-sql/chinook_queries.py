import os
import sqlite3
'''
## TablePlus and DB Brower for sqlite3
## PgAdmin for PostgreSQL
'''

#https://cdn.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf


# construct a path to wherever your database exists
# DB_FILEPATH = "module1-introduction-to-sql/chinook.db"   # / for windows \ of macOs
# DB_FILEPATH = os.path.join("module1-introduction-to-sql","chinook.db")
# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "chinook.db")

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db") 
# the .. is to go up one directory

#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "chinook.db") 
# # the .. is to go up one directory and different folder "module2-sql-for-analysis"


connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)


query = "SELECT * FROM customers;"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    print(type(row), row)


# many queries
# do them first in QueryPlus before Python Script

query = "SELECT count(distinct CustomerId) as customer_count FROM customers;"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result3 = cursor.execute(query).fetchone()
print("RESULT 3", type(result3), result3)


"""
Check Bruno video 2:00:00 in

import pandas as pd

# Get columns from cursor object

"""