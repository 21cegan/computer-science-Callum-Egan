import sqlite3

db_connection = sqlite3.connect("spurs_database.csv")

cursor = db_connection.cursor()

createTable = '''create table if not exists users(
id integer primary key autoincrement,
player text not null,
year integer,
appearances integer,
goals integer  
) STRICT'''


cursor.execute(createTable)
db_connection.commit() 


addData = '''insert into users (player,year,appearances,goals) values (?,?,?,?)'''

y = open('Spurs_data.csv','r')
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

name = rowsInTable[0][1]
total_appearances = 0
total_goals = 0
for row in rowsInTable:
    #print(row)
    if name == row[1]:
        total_appearances += row[3]
        total_goals += row[4]
    else:
        print(f"{name} has scored a total of {total_goals} over {total_appearances} matches, with an average of {round((total_goals / total_appearances),2)} goals per match")
        name = row[1]
        total_appearances = 0
        total_goals = 0
    
cursor.close()
db_connection.close() 

