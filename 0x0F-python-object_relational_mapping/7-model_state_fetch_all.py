#!/usr/bin/python3
"""
Task 7.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usrname, passwd, dbname)
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id)
    for record in result:
        print(': '.join([record.id, record.name]))
    
