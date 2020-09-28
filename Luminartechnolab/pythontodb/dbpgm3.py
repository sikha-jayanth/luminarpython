import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="luminarpython",
    auth_plugin = "mysql_native_password"
)
cursor=db.cursor()
sql="INSERT INTO EMPLOYEE(FNAME,LNAME,AGE,SEX,INCOME) VALUES('MANU','AJAY',24,'M',35000)"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print(e.args)

finally:
    db.close()