import sqlite3
import AvgFuncs
db_connection = sqlite3.connect("iris.db")

db_cursor = db_connection.cursor()

get_data = """
select * from irisData;
"""

db_cursor.execute(get_data)
data = cursor.fetchall()


sepal_length = []
sepal_width = []
petal_length = []
petal_width = []

for row in data:
    sepal_length.append(row[1])
    sepal_width.append(row[2])
    petal_length.append(row[3])
    petal_width.append(row[4])
    
print(f"""Sepal Length:
    mean:{AvgFuncs.mean(sepal_length)}
    median:{AvgFuncs.median(sepal_length)}
    mode:{AvgFuncs.mode(sepal_length)}
    range:{AvgFuncs.range(sepal_length)}
Sepal Width:
    mean:{AvgFuncs.mean(sepal_width)}
    median:{AvgFuncs.median(sepal_width)}
    mode:{AvgFuncs.mode(sepal_width)}
    range:{AvgFuncs.range(sepal_width)}
Petal Length:
    mean:{AvgFuncs.mean(petal_length)}
    median:{AvgFuncs.median(petal_length)}
    mode:{AvgFuncs.mode(petal_length)}
    range:{AvgFuncs.range(petal_length)}
Petal Width:
    mean:{AvgFuncs.mean(petal_width)}
    median:{AvgFuncs.median(petal_width)}
    mode:{AvgFuncs.mode(petal_width)}
    range:{AvgFuncs.range(petal_width)}
""")

db_cursor.close()
db_connection.close()