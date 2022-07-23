import sqlite3

conn = sqlite3.connect("datafile.db")

cursor = conn.cursor()

result = cursor.execute("select * from people")

print("all")
print(result.fetchall())

print("one")
print(result.fetchone())

print("get 2")
print(result.fetchmany(2))

# find someone here
print("--------- Find Someone Here ---------")
mark = cursor.execute("select * from people where name=:username", {"username": "Mark"})
print(mark.fetchall())

conn.commit()

conn.close()