#!/usr/bin/python3
"""Get a state"""


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
    n = argv[4]
    state = session.query(State).order_by(State.id).filter(State.name == n).first()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
