#!/usr/bin/python3
""" Definition of the state class """

from relationship_city import Base, City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship



class State(Base):
    """ Class State """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    city = relationship('City', backref='state', cascade='all, delete-orphan')
