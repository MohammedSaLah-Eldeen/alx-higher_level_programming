#!/usr/bin/python3
"""
Task 9.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
      'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usrname, passwd, dbname)
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = (
        session
        .query(State)
        .filter(State.name == state_name)
        .order_by(State.id)
        .first()
    )
    print(result.id if result else 'Not found')
