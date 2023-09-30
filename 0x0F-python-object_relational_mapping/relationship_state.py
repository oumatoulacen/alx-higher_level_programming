#!/usr/bin/python3
"""
First State Model
"""

from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class with id and name attributes of each state
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", overlaps="state",
            cascade="all, delete")
