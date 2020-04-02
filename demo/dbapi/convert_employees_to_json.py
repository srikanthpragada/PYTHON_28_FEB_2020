import sqlite3
import json

emps = []
con = sqlite3.connect(r"c:\classroom\feb28\hr.db")
cur = con.cursor()
cur.execute("select * from employees")

for t in cur.fetchall():
    emps.append({'id': t[0], 'fullname': t[1], 'salary': t[2], 'job': t[3]})

con.close()
json.dump(emps, open("employees.json", "wt"))
