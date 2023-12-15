#!/usr/bin/python3
"""
Task 12.
"""
import sys
from model_state import Base, State
from model_city import City
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

    result = (
        session
        .query(
            City.id.label('city_id'),
            City.name.label('city_name'),
            State.name.label('state_name')
        )
        .join(City, on=State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    for record in result:
        print(
            '{}: ({}) {}'.format(
                record.state_name,
                record.city_id,
                record.city_name
            )
        )
