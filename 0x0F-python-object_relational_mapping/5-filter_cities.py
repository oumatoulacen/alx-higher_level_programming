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
    query = "SELECT cities.name FROM cities INNER JOIN states ON \
            cities.state_id = states.id\
            where states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (stt,))
    query_rows = cur.fetchall()
    res = ''
    for row in query_rows:
        res += f"{row[0]}, "
    print(res[:-2])
    cur.close()
    conn.close()
