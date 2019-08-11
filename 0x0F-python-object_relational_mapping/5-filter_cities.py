#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa, safe from injection
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
