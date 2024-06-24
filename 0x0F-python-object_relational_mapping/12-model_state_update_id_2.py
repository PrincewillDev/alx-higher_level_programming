#!/usr/bin/python3
"""
This script changes the name of a State object
from the database hbtn_0e_6_usa
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
    # Use the session to query the database
    row = session.query(State).filter(State.id == 2)\
        .update({"name": "New Mexico"}, synchronize_session=False)
    session.commit()

finally:
    # Close the session
    session.close()
