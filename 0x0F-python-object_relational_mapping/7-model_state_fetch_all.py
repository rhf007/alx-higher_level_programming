#!/usr/bin/python3
"""All states via SQLAlchemy"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                      argv[2], argv[3])
    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for row in session.query(State).order_by(State.id).all():
        print("{}: {}".format(row.id, row.name))
