import sqlite3

con = sqlite3.connect(r"e:\classroom\python\demo.db")
cur = con.cursor()
try:
    cur.execute("select * from books order by title")
    for book in cur.fetchall():
        print("%-30s %-30s %4d" % (book[1], book[2],book[3]))

except Exception as ex:
    print("Error :", ex)

con.close()

