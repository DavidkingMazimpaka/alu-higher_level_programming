#!/usr/bin/python3
"""
Listing the states
"""
import MySQLdb
import sys


def list_states():
    """
    listing the states from database
    Arguments
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor_setter = db.cursor()

    cursor_setter.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor_setter.fetchall()
    for i in rows:
        print(i)

    cursor_setter.close()
    db.close()


if __name__ == "__main__":
    list_states()
