#!/usr/bin/python3
"""Add a new state"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
engine = create_engine(uri)
Session = sessionmaker()
session = Session(bind=engine)
lois = State(name='Louisiana')
session.add(lois)
session.commit()
print("{}".format(lois.id))
