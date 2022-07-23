import sqlite3

connection = sqlite3.connect("datafile.db")

cursor = connection.cursor()

cursor.execute("""create table people (id integer primary key, name text, count integer)""")

cursor.execute("""insert into people (name, count) values ("bob", 15)""")

cursor.execute("""insert into people (name, count) values (?, ?)""", ("Mark", 25))

cursor.execute("""insert into people (name, count) values (:username, :usercount)""", {"username": "Joy", "usercount": 25})

connection.commit()

connection.close()