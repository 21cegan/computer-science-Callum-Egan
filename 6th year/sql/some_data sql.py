import sqlite3

db_connection = sqlite3.connect("testdatabase.csv")

cursor = db_connection.cursor()

createTable = '''create table if not exists users(
id integer primary key autoincrement,
name text not null,
department text,
salary integer  
) STRICT'''


cursor.execute(createTable)
db_connection.commit() 


addData = '''insert into users (name,department,salary) values (?,?,?)'''

y = open('some_data.csv','r')
y.readline() #read in the header line which has no data for the table
for line in y:
    line = line.strip() # remove the newline character
    db = tuple(line.split(',')) #create a tuple for the database
    #create a docstring which contains the SQL command for the cursor to run
    cursor.execute(addData,db)
    #save the changes to the database
    db_connection.commit()
    
    
fetchData = '''select * from users'''
cursor.execute(fetchData)
#cursor.fetchall() retrieves all the remaining #rows of the table. If there are no  rows it
#returns an empty list
rowsInTable = cursor.fetchall()
for row in rowsInTable:
    print(row)
    
cursor.close()
db_connection.close() 
