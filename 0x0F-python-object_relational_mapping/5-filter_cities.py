#!/usr/bin/python3
"""All cities by state module"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute('SELECT cities.name FROM cities JOIN states ON'
                ' cities.state_id = states.id WHERE states.name = %s;',
                (argv[4],))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[0])
    print(", ".join(cities))
