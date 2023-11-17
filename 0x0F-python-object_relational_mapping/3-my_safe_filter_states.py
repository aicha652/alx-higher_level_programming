#!/usr/bin/python3
"""script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""

import MySQLdb
import sys
conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                       passwd="root", db="hbtn_0e_0_usa", charset="utf8")
name = sys.argv[4]
cur = conn.cursor()
query = "SELECT * FROM states WHERE name = %s"
cur.execute(query, (name,))
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
