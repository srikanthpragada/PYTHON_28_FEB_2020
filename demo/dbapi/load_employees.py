# Load data from employees.txt into EMPLOYEES table - one line is one row
import sqlite3

con = sqlite3.connect(r"c:\classroom\feb28\hr.db")
cur = con.cursor()

emps = []
f = open("employees.txt", "rt")
for line in f:
    cols = line.strip().split(",")
    emps.append(cols)

f.close()

# print(emps)

cur.executemany("insert into employees (fullname,salary,job) values(?,?,?)", emps)

print(f"Inserted {cur.rowcount} row(s)")
con.commit()  # Commit transaction / Save changes
con.close()
