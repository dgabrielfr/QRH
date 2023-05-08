"""
Demonstration de l'utilisation de GeoAlchemy 2
Définition de la table Airport
"""
__author__ = "Damien GABRIEL"

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geography

Base = declarative_base()


class Airport(Base):
    __tablename__ = 'airport'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    icao = Column(String)
    iata = Column(String)
    coordinates = Column(Geography('POINT', srid=4326))
