#!/usr/bin/python3
"""Create a city class"""
from model_state import Base
from sqlalchemy import ForeignKey, Column, Integer, String, UniqueConstraint


class City(Base):
    """Define a city class"""

    __tablename__ = "cities"
    # links to the MySQL table cities
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
