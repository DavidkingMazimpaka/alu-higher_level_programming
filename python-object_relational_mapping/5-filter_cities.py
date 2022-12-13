#!/usr/bin/python3
"""
Define module in current file
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3],
        'port': 3306
    }
    db = MySQLdb.connect(**db_config)
    cursor = db.cursor()
    query = """ SELECT
                       cities.name
                   FROM
                       cities
                   INNER JOIN states ON
                       cities.state_id = states.id
                   WHERE
                       states.name = %s
                   ORDER BY cities.id
               """
    cursor.execute(query, (sys.argv[4],))
    cities = list(cursor.fetchall())
    for i, city in enumerate(cities):
        print(city[0], end='')
        if i < len(cities) - 1:
            print(', ', end='')
    print('')
    cursor.close()
    db.close()
