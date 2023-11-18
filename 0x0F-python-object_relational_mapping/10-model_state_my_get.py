#!/usr/bin/python3
"""script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).filter(State.name.like(f'%{name}%')).all()
    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
