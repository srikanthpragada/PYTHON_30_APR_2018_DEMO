import sqlite3

con =  sqlite3.connect(r"e:\classroom\python\test.db")
cur = con.cursor()

# List expenses
try:
    cur.execute("select * from expenses order by id")
    for row in cur.fetchall():
    #print(row)
        print(row[0], row[1], row[2], row[3])
    else:
        cur.close()
except Exception as ex:
    print("Sorry! Error : ", ex);

finally:
    con.close()