import sqlite3

#this code will show the data.db all datas on the emp table

conn = sqlite3.connect('data.db')

cursor = conn.cursor()

select_sql = "SELECT * FROM emp;"

cursor.execute(select_sql)

rows = cursor.fetchall()

if rows:
    print("Emp Data:")
    for row in rows:
        print(f"Emp ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Phone number: {row[3]}, Phone: {row[4]}, email: {row[5]}, password: {row[6]}")
else:
    print("No Emps found.")

conn.close()