import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(150))
    favorite = relationship('Favorites', back_populates='user')

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='favorites')

    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    character = relationship('Character', back_populates='favorites')

    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    planet = relationship('Planet', back_populates='favorites')

    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    vehicle = relationship('Vehicle', back_populates='favorites')

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    gender = Column(String(15), nullable=True)
    birth_date = Column(String(100), nullable=True)
    description = Column(String(500), nullable=False)
    url = Column(String(150), nullable=False)

    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    planet = relationship('Planet', back_populates='characters')

    favorite = relationship('Favorite', back_populates='character')
    vehicle = relationship('Vehicle', back_populates='character')

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(500), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=True)

    favorite = relationship('Favorites', back_populates='planet')
    character = relationship('Character', back_populates='planet')

class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    model = Column(String(100), nullable=True)
    description = Column(String(500), nullable=False)
    capacity = Column(Integer, nullable=False)

    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    character = relationship('Character', back_populates='vehicle')

    favorite = relationship('Favorites', back_populates='vehicle')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')