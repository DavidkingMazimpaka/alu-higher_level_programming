#!/usr/bin/python3
"""
a script that prints the first State
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State.id, State.name).first()
    if res is None:
        print("Nothing")
    else:
        print("{:d}: {}".format(res[0], res[1]))
