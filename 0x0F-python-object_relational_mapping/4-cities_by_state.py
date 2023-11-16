#!/usr/bin/python3
"""module: Cities by states"""


import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], port=3306,
                     db=argv[3])
cur = db.cursor()
cur.execute('SELECT cities.id, cities.name, states.name FROM cities'
            ' JOIN states ON cities.state_id = states.id;')
rows = cur.fetchall()
for row in rows:
    print(row)
