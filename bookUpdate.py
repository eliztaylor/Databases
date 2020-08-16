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

#Change id 3 to review = N
my_cursor.execute("UPDATE books SET review = 'N' WHERE id = 3")
#Must commit for changes to take effect permanently
mydb.commit()
#Select to see changes
my_cursor.execute("SELECT title, author, review from books WHERE id = 3")



#Loop to view tables
for db in my_cursor:
	print(db)