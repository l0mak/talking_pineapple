from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import postgres_conn_string

connection = postgres_conn_string

db = create_engine(connection)
base = declarative_base()


class CommandsTable(base):
    __tablename__ = 'commands'

    id = Column(Integer, primary_key=True)
    server = Column(Integer)
    channel = Column(Integer)
    author = Column(Integer)
    command = Column(String)
    timestamp = Column(DateTime)


class MythicListTable(base):
    __tablename__ = 'mythiclist'

    id = Column(Integer, primary_key=True)
    server = Column(Integer)
    uid = Column(Integer)
    role = Column(Integer)
    timestamp = Column(DateTime)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Example
# doctor_strange = Film(title="Doctor Strange", director="Scott Derrickson", year="2016")
# session.add(doctor_strange)
# session.commit()
#
# films = session.query(Film)
# for film in films:
#     print(film.title)
#
# doctor_strange.title = "Some2016Film"
# session.commit()
#
# session.delete(doctor_strange)
# session.commit()