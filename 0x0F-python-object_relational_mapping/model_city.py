#!/usr/bin/python3
"""Cities in state"""


from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy import ForeignKey


class City(Base):
    """city class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
