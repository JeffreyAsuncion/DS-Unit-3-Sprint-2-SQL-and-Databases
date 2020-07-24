import pandas as pd 
import os
import sqlite3
from sqlalchemy import create_engine

'''
Load the data (use pandas) from the provided file buddymove_holidayiq.csv (the BuddyMove Data Set) 
- you should have 249 rows, 7 columns, and no missing values. 
The data reflects the number of place reviews by given users across a variety 
of categories (sports, parks, malls, etc.).

Using the standard sqlite3 module:

- Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
- Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database
Then write the following queries (also with sqlite3) to test:

- Count how many rows you have - it should be 249!
- How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
- (Stretch) What are the average number of reviews for each category?
Your code (to reproduce all above steps) should be saved in buddymove_holidayiq.py, 
and added to the repository along with the generated SQLite database.
'''

df = pd.read_csv("buddymove_holidayiq.csv")
# This code block is to have a quick look 
# print(df.head(5))
# print(df.shape)


# Part 1
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddmove_holidayiq.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)


# Part 2
engine = create_engine('sqlite://', echo=False)


df.to_sql("review", con=engine, if_exists = 'replace', index=False)
# This is to compare to the df.head() 
# print("My test of df.head() == SELECT * FROM buddmove_holidayiq")
# result = engine.execute("SELECT * FROM review").fetchmany(5)
# for row in result:
#     print(row)

# 1. Count how many rows you have - it should be 249!
print("\n1. Count how many rows you have.")
result1 = engine.execute("SELECT COUNT(*) FROM review").fetchone()
print("Number of row : ", result1)


# 2. How many users who reviewed at least 100 Nature in the category 
# ....also reviewed at least 100 in the Shopping category?

print("\n2. How many users who reviewed at least 100 Nature in the category")
print("    also reviewed at least 100 in the Shopping category?")

query2 = "SELECT COUNT(*) as user_count FROM review WHERE Nature >= 100 AND Shopping >=100;"
result2 = engine.execute(query2).fetchone()
print("Number of User : ", result2)


##########################Fix this open the same way in rpg_db.py
