#!/usr/bin/python3
"""script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys
conn = MySQLdb.connect(user="root", passwd="root", db="hbtn_0e_0_usa")
name = sys.argv[4]
cur = conn.cursor()
query = "SELECT * FROM states WHERE name = '{}'".format(name)
cur.execute(query)
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
