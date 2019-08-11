#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                    LEFT JOIN states ON states.id = cities.state_id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (argv[4],))
    rows = cursor.fetchall()
    print(", ".join([location[0] for location in rows]))
