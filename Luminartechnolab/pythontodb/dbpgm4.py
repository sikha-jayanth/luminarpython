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
    cursor.execute("SELECT * FROM EMPLOYEE")
    result=cursor.fetchone()  # returns result in tuples
    for x in result:
        print(x)
except Exception as e:
    print(e.args)
finally:
    db.close()
