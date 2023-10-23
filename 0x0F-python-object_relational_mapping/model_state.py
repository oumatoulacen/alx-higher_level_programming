#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base
'''Write a python file that contains the class definition
of a State and an instance Base'''

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
