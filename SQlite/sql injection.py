import sqlite3

conn = sqlite3.connect("datafile.db")

cursor = conn.cursor()

name = input("Type name you want to search: ")

# not safe
result = cursor.execute(f"""select * from people where name = '{name}'""")

# safe way
result_good = cursor.execute("""select * from people where name = :username""", {"username": name})

# 1' OR '1'='1

print(result.fetchall())

conn.commit()

conn.close()
