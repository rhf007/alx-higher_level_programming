#!/usr/bin/python3
"""module for listing all states with N"""


import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], port=3306,
                     db=argv[3])
cur = db.cursor()
stmt = "SELECT * FROM states WHERE name LIKE BINARY 'N%'"
cur.execute(stmt)
rows = cur.fetchall()
for row in rows:
    print(row)
