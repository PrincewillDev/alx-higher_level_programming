#!/usr/bin/python3
"""
This script contains a function that lists all states from a database..
Note: database name is passed as argument to the script.
"""
if __name__ == "__main__":

    import sys
    import MySQLdb

    # Assigning the arguments with their index
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    query = "SELECT * FROM states ORDER BY states.id ASC"

    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for r in result:
        print(r)

    cursor.close()
    db.close()
