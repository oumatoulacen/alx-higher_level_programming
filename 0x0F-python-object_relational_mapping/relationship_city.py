#!/usr/bin/python3
"""
Defines a city module that contain the class definition
 of a City model
"""
from sqlalchemy import Column, ForeignKey, Integer, String, null
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """ City model"""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
