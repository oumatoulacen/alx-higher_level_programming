#!/usr/bin/python3

''' modules '''
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stt = sys.argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
            )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name=%s \
            ORDER BY id ASC"
    cur.execute(query, (stt,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
