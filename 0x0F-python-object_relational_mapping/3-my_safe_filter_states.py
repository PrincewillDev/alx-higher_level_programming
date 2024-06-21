#!/usr/bin/python3

"""
This script takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    pword = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db_conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=pword,
        db=db_name
    )

    cursor = db_conn.cursor()

    query = "SELECT * FROM states WHERE BINARY name = %s"

    cursor.execute(query, (state,))

    row = cursor.fetchall()
    for item in row:
        print(item)

    cursor.close()
    db_conn.close()
