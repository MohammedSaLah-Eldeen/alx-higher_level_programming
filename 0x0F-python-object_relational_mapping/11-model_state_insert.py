#!/usr/bin/python3
"""
Task 11.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
