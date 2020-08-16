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

#Create new table reviews using Foreign key from books db
my_cursor.execute("CREATE TABLE reviews (reviewID int PRIMARY KEY AUTO_INCREMENT, titleID int (2), review VARCHAR(255), stars int(2))")
my_cursor.execute("SHOW TABLES")

#Loop to view tables
for db in my_cursor:
	print(db)