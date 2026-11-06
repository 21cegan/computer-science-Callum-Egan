import sqlite3

db_connection = sqlite3.connect("iris.db")

db_cursor = db_connection.cursor()

createTable ="""create table if not exists irisData(
sepal_id INTEGER PRIMARY KEY AUTOINCREMENT,
sepal_len REAL NOT NULL,
sepal_wid REAL NOT NULL,
petal_len REAL NOT NULL,
petal_wid REAL NOT NULL,
class INTEGER NOT NULL
) STRICT

"""

db_cursor.execute(createTable)
db_connection.commit()

db_cursor.close()
db_connection.close()