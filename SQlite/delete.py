import sqlite3

conn = sqlite3.connect("datafile.db")

cursor = conn.cursor()

cursor.execute("""Delete from people where name='bob'""")

result = cursor.execute("select * from people")

print("all")
print(result.fetchall())

conn.commit()

conn.close()
 