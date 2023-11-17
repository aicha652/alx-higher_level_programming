#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
conn = MySQLdb.connect(user="root", passwd="root", db="hbtn_0e_4_usa")
cur = conn.cursor()
cur.execute("SELECT cities.id, cities.name, states.name FROM cities,states \
        WHERE states.id = cities.state_id ORDER BY cities.id ASC")
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
