#!/usr/bin/python3
"""
Task 6.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, MetaData


metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """
    model - states
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
