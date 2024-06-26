#!/usr/bin/python3

"""
This script takes in the name of a state as an
argument and lists all cities of that state,
using the database
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    pword = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db_conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, password=pword, db=db_name
    )

    cursor = db_conn.cursor()

    query = """
    SELECT cities.name
    FROM cities JOIN states
    ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state,))

    row = cursor.fetchall()
    print(", ".join(item[0] for item in row))

    cursor.close()
    db_conn.close()
