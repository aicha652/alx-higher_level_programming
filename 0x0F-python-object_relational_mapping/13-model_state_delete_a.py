#!/usr/bin/python3
""" script that changes the name of a State
object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    session.query(
            State
            ).filter(
                    State.name.like('%a%')
                    ).delete(synchronize_session=False)

    session.commit()
