import sqlite3

con = sqlite3.connect(r"e:\classroom\python\demo.db")
cur = con.cursor()
try:
    id = input("Enter book id :")
    price = input ("Enter new price : ")
    cur.execute("update books set price = ? where bookid = ?", (price,id))
    if cur.rowcount == 1:
        print("Updated Successfully!")
        con.commit()
    else:
        print("Sorry! Book not found!")
except Exception as ex:
    print("Error :", ex)

con.close()

