import os
import pandas as pd 
from dotenv import load_dotenv
import psycopg2



# STEP ONE : IMPORT THE CSV INTO A DATAFRAME

df = pd.read_csv("titanic.csv")
# HAVE A LOOK AT THE COLUMN NAMES AND TYPES
print(df.head())


# STEP TWO : CONNECT PYTHON TO SQL SERVER
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, 
                              user=DB_USER, 
                              password=DB_PASS, 
                              host=DB_HOST)
cursor = connection.cursor()
print("CURSOR: " , cursor)


# STEP THREE : CREATE A TABLE IN SQL SERVER USING PYTHON




create_titanic_table_query = '''
CREATE TABLE IF NOT EXISTS titantic_table (
    index INT,
    survived INT,
    pclass INT,
    name VARCHAR(30),
    sex VARCHAR(1),
    age INT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare  FLOAT
)'''

cursor.execute(create_titanic_table_query)




# STEP FOUR : INSERT THE DATAFRAME INTO THE TABLE

for row in df.itertuples():

    cursor.execute('''INSERT INTO titantic_table 
    (index, survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ''',(
    row[0], 
    row[1], 
    row[2], 
    row[3], 
    row[4], 
    row[5], 
    row[6], 
    row[7], 
    row[8])
    )
    
    # test it first in print()
    # print(insert_query)
    #then use cursor
    cursor.execute(insert_query)



# STEP FIVE : COMMIT CHANGES
connection.commit()