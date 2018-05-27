import sqlite3

con =  sqlite3.connect("c:\\dev\\python\\test.db")
cur = con.cursor()

# insert a row
try:
    # take data from user
    id =   input("Enter id :");
    date = input("Enter Date [yyyy-mm-dd] :")
    desc = input("Enter Description       :")
    amt  = input("Enter Amount            :")

    row = (id,date,desc,amt)
    cur.execute("insert into expenses values(?,?,?,?)", row)
    con.commit()
    print("Added row to EXPENSES table successfully!")
except Exception as ex:
    print("Sorry! Error : ", ex);

finally:
    con.close()