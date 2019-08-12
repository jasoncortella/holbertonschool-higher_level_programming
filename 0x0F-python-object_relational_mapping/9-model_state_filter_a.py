#!/usr/bin/python3
"""
lists all state objects from the database hbtn_0e_6_usa
that contain the letter a
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
