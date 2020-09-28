import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="luminarpython",
    auth_plugin = "mysql_native_password"
)
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEEE")
sql="CREATE TABLE EMPLOYEE(FNAME VARCHAR(20),LNAME VARCHAR(20),AGE INT, SEX CHAR(1),INCOME FLOAT)"
cursor.execute(sql)
db.close()