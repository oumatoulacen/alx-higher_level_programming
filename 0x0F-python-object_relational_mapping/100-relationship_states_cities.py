#!/usr/bin/python3
""" creates the State “California” with the City “San Francisco” from the
database hbtn_0e_100_usa"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base

engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
    argv[1], argv[2], argv[3])
)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
state = State(name="California")
city = City(name="San Francisco", state=state)
session.add(state)
session.add(city)
session.commit()
