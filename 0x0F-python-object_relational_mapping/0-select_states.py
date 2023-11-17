#!/usr/bin/python3
"""module for selecting states"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """lets try using this way to see if something is fixed"""
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         port=3306, db=argv[3])
    cur = db.cursor()
    stmt = "SELECT * FROM states"
    cur.execute(stmt)
    rows = cur.fetchall()
    for row in rows:
        print(row)
