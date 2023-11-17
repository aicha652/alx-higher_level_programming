#!/usr/bin/python3
import MySQLdb
conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                       passwd="root", db="hbtn_0e_4_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT cities.id, cities.name, states.name FROM cities,states \
        WHERE states.id = cities.state_id ORDER BY cities.id ASC")
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
