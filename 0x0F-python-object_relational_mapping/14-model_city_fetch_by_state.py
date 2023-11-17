#!/usr/bin/python3
"""Cities in state"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from model_city import City

uri = uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
engine = create_engine(uri)
Session = sessionmaker()
session = Session(bind=engine)
for s, c in session.query(State, City).filter(State.id == City.state_id).all():
    print("{}: ({}) {}".format(s.name, c.id, c.name))
