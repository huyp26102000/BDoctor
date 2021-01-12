import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lemon"
)

print(mydb)