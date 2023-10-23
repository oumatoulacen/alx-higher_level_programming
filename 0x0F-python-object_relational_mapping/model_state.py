#!/usr/bin/python3
'''Write a python file that contains the class definition'''

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base()


class State(Base):
    '''A state object that represents a state'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
