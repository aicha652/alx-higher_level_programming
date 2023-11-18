#!/usr/bin/python3
""" script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':  # The code should not be executed when imported
    # Get this parametrs from the command line argument
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    # Connect to a MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")

    # Create a cursor object to execute sql queries
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities, states WHERE \
            cities.state_id = states.id and states.name = %s ORDER BY cities.id ASC"

    # Execute the query
    cur.execute(query, (name,))

    # Fetch all the matching rows
    query_rows = cur.fetchall()

    # Display the results
    cities = ', '.join(row[0] for row in query_rows)
    print(cities)

    # Close the cirsor and the database connection
    cur.close()
    conn.close()
