#!/usr/bin/python3
"""
 a script that prints the State object with the name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def arg_State():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).all()

    res = ""

    for i in rows:
        if sys.argv[4] in i.__dict__['name']:
            res = i.__dict__['id']

    if res != "":
        print(res)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    arg_State()
