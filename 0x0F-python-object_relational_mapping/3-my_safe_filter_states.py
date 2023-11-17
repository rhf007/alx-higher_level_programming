#!/usr/bin/python3
"""module: Filter states by user input but safer cuz we're cool"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], port=3306,
                         db=argv[3])
    cur = db.cursor()
    state = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
