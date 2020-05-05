# tablice w bazie danych dla wszystkich danych stacji (stacje, miasta, sensory, parametry)

import sqlalchemy
from sqlalchemy import *

from engine import engine

metadata = MetaData()

cities = Table('cities', metadata,
               Column('id', Integer, primary_key=True),
               Column('c_name', String(30), unique=True, nullable=False),
               Column('commune', String(30), nullable=False),
               Column('district', String(30), nullable=False),
               Column('province', String(30), nullable=False)
               )

stations = Table('stations', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('st_name', String(60), unique=True, nullable=False),
                 Column('gegr_lat', Float, nullable=False),
                 Column('gegr_lon', Float, nullable=False),
                 Column('city_id', Integer, ForeignKey(
                     'cities.id'), nullable=False),
                 Column('street', String(60))
                 )

params = Table('params', metadata,
               Column('id', Integer, primary_key=True),
               Column('code', String(30), unique=True, nullable=False),
               Column('formula', String(30), unique=True, nullable=False),
               Column('p_name', String(30), unique=True, nullable=False)
               )

sensors = Table('sensors', metadata,
                Column('id', Integer, primary_key=True),
                Column('param_id', Integer, ForeignKey(
                    'params.id'), nullable=False),
                Column('station_id', Integer, ForeignKey(
                    'stations.id'), nullable=False)
                )

air_data = Table('air_data', metadata,
                 Column('sensor_id', Integer, ForeignKey(
                     "sensors.id"), primary_key=True, nullable=False),
                 Column('date_s', DateTime, primary_key=True, nullable=False),
                 Column('sensor_v', Float)
                 )

quality = Table('quality', metadata,
                Column('station_id', Integer, ForeignKey(
                    'stations.id'), primary_key=True, nullable=False),
                Column('date_q', DateTime, primary_key=True, nullable=False),
                Column('level_id', Integer),
                Column('level_name', String(20))
                )

metadata.create_all(engine)
