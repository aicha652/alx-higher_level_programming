#!/usr/bin/python3
""" script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities, states WHERE cities.state_id = states.id and name = %s"
    cur.execute(query, (name,))
    # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
