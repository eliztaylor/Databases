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
reviews = [(2, "One of my favorite books. Love the story and the characters. Feels so relevant to now. Much better than movie!", 5),
			(4, "A delightful story. Characters feel so real and relatable. Makes me happy.", 4),
			(6, "Stressful, drags at times, but captivating over all. Great twist, actually more than one twist.", 4),
			(16, "Unexpected. Starts like a typical rom-com. You know exactly what is going to happen, until you don't. Great characters!", 4), 
			(17, "Kind of dark. Okay. Enjoyed it at the time, but not very memorable. Would read again.", 3), 
			(18, "Trippy and wild. You know something's off but it's not what you expect. Great characters and settings are very real.", 4), 
			(24, "Another great Riley Sager. So many twists and turns. Actually scared me at times, but it's never what you think. So good.", 5)]

#Use executemany command to insert multiple records using above variable
my_cursor.executemany("INSERT INTO reviews (titleID, review, stars) VALUES (%s, %s, %s)", reviews)
#Changes must be commited to be permanent
mydb.commit()

#Query to show data inserted
my_cursor.execute("SELECT * FROM reviews")

#Loop to view tables
for db in my_cursor:
	print(db)