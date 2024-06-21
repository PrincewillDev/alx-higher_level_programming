#!/usr/bin/python3

"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
Note: database name is passed as argument to the script.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

# Assign cmd arguments to the input

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

# Connect to DB
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        db=db_name
    )

# Create a cursor
    cursor = db.cursor()

# Create query
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY states.id"\
        .format(state)

# Execute query
    cursor.execute(query)

    rows = cursor.fetchall()
    for r in rows:
        print(r)


# Close cursor and connection
    cursor.close()
    db.close()
