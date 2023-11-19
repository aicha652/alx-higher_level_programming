#!/usr/bin/python3
"""script that that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id).order_by(City.id).all():
        # HERE: no SQL query, only objects!
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
