# zapis danych dotyczących stacji (stacje, miasta, sensory, parametry) do bazy postgresql

import pandas as pd
import sqlalchemy

from engine import engine
from gios_sensors import sensors, params
from gios_stations import stations, cities

params.to_sql('params',
                engine,
                schema='public',
                if_exists='append',
                index=False)

cities.to_sql('cities',
                engine,
                schema='public',
                if_exists='append',
                index=False)

stations.to_sql('stations',
                engine,
                schema='public',
                if_exists='append',
                index=False)

sensors.to_sql('sensors',
                engine,
                schema='public', 
                if_exists='append',
                index=False)



