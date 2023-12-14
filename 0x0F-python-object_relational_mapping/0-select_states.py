"""
Task 0.
"""
#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

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
        SELECT * FROM states;
        '''
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.clean()
    db.close()
