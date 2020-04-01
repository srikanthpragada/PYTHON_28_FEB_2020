import sqlite3


con = sqlite3.connect(r"c:\classroom\feb28\hr.db")
cur = con.cursor()
cur.execute("select * from employees order by salary desc")

for t in cur.fetchall():
    print(f"{t[1]:20}  {t[3]:5}  {t[2]:6}")

con.close()
