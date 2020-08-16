#Import mysql connector
import mysql.connector

#Create Database instance and credentials including URL of database
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "p@ssw0rd",
	database = "bookdb")

#Create instance of cursor
my_cursor = mydb.cursor()

my_cursor.execute("SHOW COLUMNS FROM books")

#my_cursor.execute("SHOW TABLES")

for db in my_cursor:
	print(db [0])