#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
if __name__ == '__main__':
    conn = MySQLdb.connect(user="root", passwd="root", db="hbtn_0e_0_usa")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
