#!/usr/bin/python3

"""
This script lists all cities from the database
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    pword = sys.argv[2]
    db_name = sys.argv[3]

    db_conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=pword,
        db=db_name
    )

    cursor = db_conn.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities JOIN states
    ON states.id = cities.state_id  ORDER BY cities.id ASC
    """

    cursor.execute(query)

    row = cursor.fetchall()
    for item in row:
        print(item)

    cursor.close()
    db_conn.close()
