from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbPath = "data3.db"
engine = create_engine("sqlite:///%s" % dbPath)
metadata = MetaData(engine)

people = Table("people", metadata,
               Column("id", Integer, primary_key=True),
               Column("name", String),
               Column("count", Integer)
               )

Base = declarative_base()


class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    count = Column("count", Integer)


Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# Add New Person
new_person_1 = People(name="Tuna", count=17)
new_person_2 = People(name="Finy", count=26)
new_person_3 = People(name="Kins", count=14)

# Add New Person
session.add(new_person_1)
session.add(new_person_2)
session.add(new_person_3)

# Update Person
leo = session.query(People).filter_by(name="Leo").first()
leo.count = 50
session.add(leo)

# Delete Person
jane = session.query(People).filter_by(name="Jane").first()
session.delete(jane)

session.commit()

for r in session.query(People).all():
    print(r.id, r.name, r.count)

for r in session.query(People).filter_by(name="Leo"):
    print(r.id, r.name, r.count)

session.close()
