from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

dbPath = "datafile2.db"

engine = create_engine("sqlite:///%s" % dbPath)
metadata = MetaData(engine)

people = Table("people", metadata, Column("id", Integer, primary_key=True), Column("name", String),
               Column("count", Integer))
Session = sessionmaker(bind=engine)
session = Session()

metadata.create_all(engine)

# Insert one
insert_statement_1 = people.insert().values(name="Tun", count=46)
session.execute(insert_statement_1)

# Insert two
insert_statement = people.insert()
session.execute(insert_statement, [
    {"name": "Alson", "count": 14},
    {"name": "Cands", "count": 12}
])

result = session.execute(select([people]))
for row in result:
    print(row)

print("--------- Find Name ---------")
find_names = session.execute(select([people]).where(people.c.name == "Leo"))
for row in find_names:
    print(row)

print("--------- Update ---------")
update_something = session.execute(people.update().values(count=55).where(people.c.name == "Leo"))
for row in update_something:
    print(row)

session.commit()
session.close()