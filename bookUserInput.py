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

#Create a variable to store review information
b_title = input("Enter book title: ")
b_author = input("Enter author name: ")
b_synopsis = input("Enter a short synopsis: ")
b_review = input("Reviewed? Enter Y or N ")
b_finished = input("Finished book? Enter Y or N ")


#Use executemany command to insert multiple records using above variable
my_cursor.execute("INSERT INTO books (title, author, synopsis, review, finished) VALUES (%s, %s, %s, %s, %s)", (b_title, b_author, b_synopsis, b_review, b_finished))

#Changes must be commited to be permanent
mydb.commit()

#Query to show data inserted
my_cursor.execute("SELECT * FROM books")

#Loop to view tables
for db in my_cursor:
	print(db)