import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "p@ssw0rd",
	database = "testdb"
	)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE testdb")
my_cursor.execute("SHOW DATABASES")

#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INT(10), user_id INT AUTO_INCREMENT PRIMARY KEY)")
#my_cursor.execute("SHOW TABLES")

#sqlstuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
#my_cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", ("Mary", "missmary@gmail.com", 37))
#mydb.commit()

#my_cursor.execute("SELECT * FROM users")

for x in my_cursor:
	print(x)

