import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE dept(deptid INT(2) not null," 
sql += "DeptName VARCHAR(15), Location VARCHAR(15),"
sql += "PRIMARY KEY (deptid))"
try:
  mycursor.execute(sql)
except:
  print("Th table dept exist")

sql = "CREATE TABLE employee" 
sql += "(Employeeld INT(3) not null, Lname VARCHAR(20), Fname VARCHAR(20),"
sql += "Salary DOUBLE(9,2), deptid INT(2) not null,"
sql += "PRIMARY KEY (Employeeld),"
sql += "FOREIGN KEY (deptid) REFERENCES dept(deptid))"
try:
  mycursor.execute(sql)
except:
  print("Th table employee exist")



