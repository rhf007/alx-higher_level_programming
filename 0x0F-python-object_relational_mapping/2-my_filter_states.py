#!/usr/bin/python3
"""module: Filter states by user input"""


import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], port=3306,
                     db=argv[3])
cur = db.cursor()
state = argv[4]
cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4]))
rows = cur.fetchall()
for row in rows:
    print(row)
