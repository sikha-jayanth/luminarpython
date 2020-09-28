import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="luminarpython",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
try:
    cursor.execute("SELECT FNAME FROM EMPLOYEE WHERE INCOME>3000")
    result=cursor.fetchall()
    for x in result:
        print(x)
except Exception as e:
    print(e.args)
finally:
    db.close()