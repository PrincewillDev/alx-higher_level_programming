#!/usr/bin/python3
"""
This script contains the class definition of
a State and an instance Base = declarative_base():
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for our models
Base = declarative_base()

# Define our User model


class State(Base):
    """Links to the states table of a MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
