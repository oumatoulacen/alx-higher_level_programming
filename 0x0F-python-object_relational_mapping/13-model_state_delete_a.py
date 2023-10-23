#!/usr/bin/python3
"""
Script to Update object in database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete from database
    states = session.query(State).filter(
        State.name.like("%a%"))
    for state in states:
        session.delete(state)
    session.commit()

    session.close()
