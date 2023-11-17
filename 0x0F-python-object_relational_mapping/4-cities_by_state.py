#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    conn = MySQLdb.connect(user=username, passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities,states \
        WHERE states.id = cities.state_id ORDER BY cities.id ASC")
    # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
