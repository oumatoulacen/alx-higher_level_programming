#!/usr/bin/python3
"""a script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    res = session.query(State).order_by(State.id, City.id).all()
    for state in res:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
    session.close()
