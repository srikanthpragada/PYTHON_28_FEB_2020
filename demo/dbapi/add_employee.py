import sqlite3

con = sqlite3.connect(r"c:\classroom\feb28\hr.db")
cur = con.cursor()

name = input("Employee fullname  :")
job = input("Employee job       :")
salary = int(input("Employee salary    :"))

cur.execute("insert into employees (fullname,salary,job) values(?,?,?)",
            (name, salary, job))

con.commit()  # Commit transaction / Save changes
con.close()
