#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    # Create a cursor
    cursor = db.cursor()

    # Query to retrieve states sorted by id
    query = "SELECT * FROM states ORDER BY id ASC"

    try:
        cursor.execute(query)
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        cursor.close()
        db.close()
        sys.exit(1)

    # Display results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
