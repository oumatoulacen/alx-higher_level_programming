#!/usr/bin/python3
"""Write a script that lists all City objects from the database
hbtn_0e_101_usa
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
    res = session.query(City).order_by(City.id).all()
    for city in res:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()
