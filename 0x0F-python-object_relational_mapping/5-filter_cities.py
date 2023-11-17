#!/usr/bin/python3
""" script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                       passwd="root", db="hbtn_0e_4_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT name FROM cities ORDER BY cities.id ASC")
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
