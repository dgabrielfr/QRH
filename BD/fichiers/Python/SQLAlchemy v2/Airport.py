"""
Demonstration de l'utilisation de GeoAlchemy 2
Définition de la table Airport
"""
__author__ = "Damien GABRIEL"

from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geography
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Airport(Base):
    __tablename__ = 'airport'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    icao: Mapped[str] = mapped_column(String(4))
    iata: Mapped[str] = mapped_column(String(3))
    coordinates: Mapped[Geography] = mapped_column(Geography('POINT', srid=4326))

