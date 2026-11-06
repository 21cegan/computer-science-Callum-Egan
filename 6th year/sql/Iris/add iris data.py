import sqlite3

db_connection = sqlite3.connect("iris.db")

db_cursor = db_connection.cursor()

addData = """ insert into irisData(sepal_len,sepal_wid,petal_len,petal_wid,class) values (?,?,?,?,?);"""


f = open("Iris - all-numbers.csv")
headerline = f.readline()

for line in f:
    line = line.strip()
    line = line.split(",")
    line = tuple(line)
    
    db_cursor.execute(addData,line)
    db_connection.commit()
    
db_cursor.close()
db_connection.close()