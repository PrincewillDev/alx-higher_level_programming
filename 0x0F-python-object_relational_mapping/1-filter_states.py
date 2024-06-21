#!/usr/bin/python3
"""
This script contains a function that lists all states
from a database starting with learner N..
Note: database name is passed as argument to the script.
"""
# Ensuring code cant execute when imported
if __name__ == "__main__":
    # Import the modules
    import sys
    import MySQLdb

    # Assigning the arguments with their index
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create Cursor
    cursor = db.cursor()

    # Fetch data from database
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                 ORDER BY states.id")
    # Use a for loop to print out the result
    rows = cursor.fetchall()
    for r in rows:
        print(r)

    # Close cursor and connection
    cursor.close()
    db.close()
