#!/usr/bin/python3
"""First state"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine

uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
engine = create_engine(uri)
Session = sessionmaker(bind=engine)
session = Session()
first = session.query(State).order_by(State.id).first()
if first is None:
    print("Nothing")
print("{}: {}".format(first.id, first.name))
