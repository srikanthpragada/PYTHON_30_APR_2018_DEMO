import sqlite3

con = sqlite3.connect(r"e:\classroom\python\demo.db")
cur = con.cursor()
try:
    cur.execute("select count(bookid), avg(price) from books")
    details = cur.fetchone()
    print("No. of books  : ", details[0])
    print("Average Price : ", details[1])
except Exception as ex:
    print("Error :", ex)

con.close()

