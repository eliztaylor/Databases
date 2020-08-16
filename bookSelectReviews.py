#Import mysql connector
import mysql.connector

#Create Database instance and credentials including URL of database
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "p@ssw0rd",
	#Add database, like mysql USE command
	database = "bookdb")

#Create instance of cursor
my_cursor = mydb.cursor()

#Show which tables in books have a yes for reviews
my_cursor.execute("SELECT id, title, author, review FROM books WHERE review = 'Y'")


#Loop to view tables
for db in my_cursor:
	print(db)