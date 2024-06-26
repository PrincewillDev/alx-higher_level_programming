#!/usr/bin/python3
"""This module contains a class City which links to a MySQL database table
'cities'.

Classes:
    City: Links to the table 'cities' of a MySQL database.

Attributes:
    None

Functions:
    None
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base, State


# Define our City model
class City(Base):

    """Links to the states table of a MySQL database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'))
