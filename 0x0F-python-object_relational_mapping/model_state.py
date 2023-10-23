#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
'''Write a python file that contains the class definition
of a State and an instance Base'''

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
