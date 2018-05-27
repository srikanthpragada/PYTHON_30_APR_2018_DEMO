# use memory database

import sqlite3

con =  sqlite3.connect(r"e:\\classroom\\python\\test.db")
cur = con.cursor()

# create a table
try:
    cur.execute("create table expenses (id integer, date text, desc  text, amount real)")
    print("Table EXPENSES created successfully!")
except Exception as ex:
    print("Sorry! Error : ", ex.message);
finally:
    con.close()





