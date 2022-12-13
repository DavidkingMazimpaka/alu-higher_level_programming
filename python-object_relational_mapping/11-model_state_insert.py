#!/usr/bin/python3
"""
 adding the State object “Louisiana” to the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def inserting_to_db():
    """
    returning the state id
    :return:
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = State(state_Name='Louisiana')

    session.add(state)
    session.commit()
    print(state.id)

    session.close()


if __name__ == "__main__":
    inserting_to_db()
