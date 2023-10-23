#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    session = sessionmaker(bind=engine)()
    res = session.query(State, City).filter(State.id == City.state_id).all()

    for s, c in res:
        print(f"{s.name}: {c.id} {c.name}")
