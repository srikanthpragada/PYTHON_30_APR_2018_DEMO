import os
import cx_Oracle

# folder where instant client is placed
os.environ['PATH'] =r'c:\oraclexe\instantclient_12_2'
con = cx_Oracle.connect("hr/hr@localhost")

cur = con.cursor()
cur.execute("select job_id,job_title from jobs")

for job in cur.fetchall():
    print(job[1])

cur.close()
con.close()