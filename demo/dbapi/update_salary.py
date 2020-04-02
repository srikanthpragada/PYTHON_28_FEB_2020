import sqlite3

try:
    with sqlite3.connect(r"c:\classroom\feb28\hr.db") as con:
        cur = con.cursor()

        id = int(input("Employee id            :"))
        salary = int(input("Employee new salary    :"))

        cur.execute("update employees set salary = ? where id = ?", (salary, id))

        if cur.rowcount == 1:
            print("Updated salary successfully!")
            con.commit()  # Commit transaction / Save changes
        else:
            print("Sorry! Employee Id not found!")
except Exception as ex:
    print("Sorry! Database error :", ex)
