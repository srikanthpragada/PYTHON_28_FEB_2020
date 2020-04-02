import sqlite3

try:
    with sqlite3.connect(r"c:\classroom\feb28\hr.db") as con:
        cur = con.cursor()

        id = int(input("Employee id            :"))
        cur.execute("delete from employees where id = ?", (id,))

        if cur.rowcount == 1:
            print("Deleted employee successfully!")
            con.commit()  # Commit transaction / Save changes
        else:
            print("Sorry! Employee Id not found!")
except Exception as ex:
    print("Sorry! Database error :", ex)
