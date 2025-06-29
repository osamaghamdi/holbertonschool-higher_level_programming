#!/usr/bin/python3
"""
Updates the name of the State with id=2 to 'New Mexico'
in the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True
    )

    session = Session(engine)

    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
