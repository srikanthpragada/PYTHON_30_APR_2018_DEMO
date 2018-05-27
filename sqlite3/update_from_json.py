import sqlite3
import json

con = sqlite3.connect("c:\\dev\\python\\test.db")
cur = con.cursor()

try:

    f = open("new_prices.txt", "rt")
    data = json.load(f)
    for info in data:

        values = (info["price"], info["id"])
        cur.execute("update products set price = ? where id = ?", values)
        if cur.rowcount == 1:
            print("Updated Successfully!")

        else:
            # insert
            values= (info["id"], info["name"], info["price"])
            cur.execute("insert into  products values(?,?,?,0)", values)
            print("Inserted!")

    else:
        con.commit()
except Exception as ex:
    con.rollback()
    print("Sorry! Error : ", ex);

finally:
    con.close()
