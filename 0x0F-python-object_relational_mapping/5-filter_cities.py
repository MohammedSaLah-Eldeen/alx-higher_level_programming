#!/usr/bin/python3
"""
Task 5.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=usrname,
        passwd=passwd,
        db=dbname
    )

    cur = db.cursor()
    cur.execute(
        '''
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        WHERE states.name = '{}'
        ORDER BY cities.id
        '''.format(state_name)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
