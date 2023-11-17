#!/usr/bin/python3
"""script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
conn = MySQLdb.connect(user="root", passwd="root", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
