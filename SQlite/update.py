import sqlite3

conn = sqlite3.connect("datafile.db")

cursor = conn.cursor()

cursor.execute("""update people set count = :usercount where name = :username""", {"username": "Mark", "usercount": 28})

result = cursor.execute("select * from people where name=:username", {"username": "Mark"})

print(result.fetchall())

conn.commit()
conn.close()
