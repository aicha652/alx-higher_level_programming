#!/usr/bin/python3
"""Define a class State"""
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Create a class State"""
    __tablename__ = 'states'  # links to the MySQL table states
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
