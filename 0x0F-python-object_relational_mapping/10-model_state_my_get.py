#!/usr/bin/python3
"""
This script prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
using sqlalchemy
"""

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

# Assigning the arguments with their index
try:
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]

except IndexError:
    print(f"Usage: {sys.argv[0]} <username> <password> <databasename>")
    sys.exit(1)

# Create engine
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'
    .format(username, password, dbname), pool_pre_ping=True
    )
# Base.metadata.create_all(engine)

# Create Session Class
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Create query
    data = session.query(State.id).filter(State.name == state)\
        .scalar()

    if data:
        print(data)
    else:
        print("Not found")

finally:
    # Close the session
    session.close()
