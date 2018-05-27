import sqlite3

con = sqlite3.connect(r"e:\classroom\python\demo.db")
cur = con.cursor()
try:
    cur.execute("update books set price = price * 1.1 where bookid = 1")
    if cur.rowcount == 1:
        print("Updated Successfully!")
        con.commit()
    else:
        print("Sorry! Book not found!")
except Exception as ex:
    print("Error :", ex)

con.close()

