import sqlite3

con =  sqlite3.connect("c:\\dev\\python\\test.db")
cur = con.cursor()

# insert a row
try:
    # take data from user
    id =   input("Enter id :");
    amt  = input("Enter Nnew Amount :")

    values = (amt,id)
    cur.execute("update expenses set amount = ? where id = ?", values)
    if cur.rowcount == 1:
        print("Updated Successfully!")
        con.commit()
    else:
        print("Id not found!")

except Exception as ex:
    print("Sorry! Error : ", ex);

finally:
    con.close()