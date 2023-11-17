#!/usr/bin/python3
"""Delete states"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(uri)
    Session = sessionmaker()
    session = Session(bind=engine)
    for s in session.query(State).filter(State.name.like('%a%')):
        session.delete(s)
    session.commit()
