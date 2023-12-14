#!/usr/bin/python3
"""
Task 2.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name_searched = sys.argv[4]

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
        SELECT * 
        FROM states
        WHERE BINARY states.name = '{}'
        ORDER BY states.id
        '''.format(state_name_searched)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
