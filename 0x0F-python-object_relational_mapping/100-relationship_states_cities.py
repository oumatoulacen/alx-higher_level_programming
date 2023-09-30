#!/usr/bin/python3
'''
 creates the State “California” with the City “San Francisco”
 from the database hbtn_0e_100_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    session.add(california)

    san_fransisco = City(name="San Francisco", state=california)
    session.add(san_francisco)
    
    session.commit()

    session.close()


