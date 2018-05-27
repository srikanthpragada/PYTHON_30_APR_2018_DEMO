import os
import cx_Oracle


os.environ['PATH'] =r'c:\oraclexe\instantclient_12_2'
con = cx_Oracle.connect("hr/hr@localhost")

cur = con.cursor()
cur.execute("update jobs set job_title = :title where job_id = :id",
                id='JAVA_PROG', title="Java 10 Programmer")
print("Updated Job Successfully!")
cur.close()
con.commit()
con.close()