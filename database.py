import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senhateste",
  database='python-tkinter'
)

print(mydb)