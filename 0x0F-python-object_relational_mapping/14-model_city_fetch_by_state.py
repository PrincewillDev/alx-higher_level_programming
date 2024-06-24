#!/usr/bin/python3
"""This script prints all City objects from the database hbtn_0e_14_usa.
Database name is passed as an argument to the script.
"""

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

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
    rows = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(asc(City.id)).params(state_id=State.id).all()

    for city, state in rows:
        print(f"{state.name}: ({city.id}) {city.name}")
finally:
    # Close the session
    session.close()
