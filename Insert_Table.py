import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mcursor = mydb.cursor()

sql = "INSERT INTO dept (deptid, DeptName, Location) VALUES (%s, %s, %s)"
val = [
  (1, 'Human Resources', 'st. remi'),
  (2, 'Accounting', 'st. remi'),
  (3, 'Computer', 'st. remi')
]

try:
 mcursor.executemany(sql, val)
except:
  print("The departments exist")

mydb.commit()

sql = "SELECT * from dept"
mcursor.execute(sql)
mresult = mcursor.fetchall()

for x in mresult:
  print(x)
