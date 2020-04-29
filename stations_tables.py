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
    Column('city_id', Integer, ForeignKey('cities.id'), nullable=False),
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
    Column('param_id', Integer, ForeignKey('params.id'), nullable=False),
    Column('station_id', Integer, ForeignKey('stations.id'), nullable=False)
)

metadata.create_all(engine)