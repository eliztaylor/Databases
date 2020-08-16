#Import mysql connector
import mysql.connector

#Create Database instance and credentials including URL of database
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "p@ssw0rd",
	)

#Create instance of cursor
my_cursor = mydb.cursor()

#SQL command to show available databases
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
	print(db [0])