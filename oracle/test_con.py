import os
import cx_Oracle

os.environ['PATH'] = r'c:\oraclexe\instantclient_12_2'
con = cx_Oracle.connect("hr","hr", "localhost/xe")
print("Connected!")
con.close()