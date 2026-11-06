import sqlite3

#Connect to a database
#This will create an empty file on your computer with the name of the database
#if the file does not already exist
db_connection = sqlite3.connect("mydatabase.db")

#create a cursor object
cursor = db_connection.cursor()

#create a docstring which contains the SQL command for the cursor to run
createTable = '''create table if not exists users(
id integer primary key autoincrement,
name text not null,
age integer  
) STRICT'''

#Execute the SQL command 
#This will create an empty table in our database 
cursor.execute(createTable) #run the SQL command
db_connection.commit() #save the change to the database

#create a docstring which contains the SQL command for the cursor to run
addData = '''insert into users (name,age) values (?,?)'''
cursor.execute(addData,('John',40))
#save the changes to the database
db_connection.commit()

#create a docstring which contains the SQL command for the cursor to run
fetchData = '''select * from users'''
cursor.execute(fetchData)
#cursor.fetchall() retrieves all the remaining #rows of the table. If there are no  rows it
#returns an empty list
rowsInTable = cursor.fetchall()
for row in rowsInTable:
    print(row)
    
cursor.close()
db_connection.close()