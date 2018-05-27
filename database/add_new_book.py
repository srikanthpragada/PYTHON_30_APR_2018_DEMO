import sqlite3

con = sqlite3.connect(r"e:\classroom\python\demo.db")
cur = con.cursor()
try:
    id = input("Enter book id :")
    title = input ("Enter title : ")
    author = input("Enter author : ")
    price =  input("Enter price : ")
    cur.execute("insert into books values(?,?,?,?)", (id,title,author,price))
    if cur.rowcount == 1:
        print("Added Book Successfully!")
        con.commit()
    else:
        print("Sorry! Could not add book!")
except Exception as ex:
    print("Error :", ex)

con.close()

