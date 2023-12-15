#!/usr/bin/python3
"""
Task 7.
"""
import sys
from mysqlalchemy import create_engine
from mysqlalchemy import select
from mysqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(f'mysql://{usrname}:{passwd}@localhost:3306/{dbname}')
    Session = sessionmaker(bind=engine)
    session = Session()

    result = select(State).order_by(State.id)
    for record in result:
        print(': '.join([record.id, record.name]))
    
