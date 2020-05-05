""" Loads data from sensors to table 'air_data """

import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

from engine import engine
from air_data import load_s

""" List of sensors ids in province Wielkopolska. """
sensors_wielkopol = pd.read_sql("SELECT cities.c_name, sensors.id FROM sensors INNER JOIN stations ON sensors.station_id = stations.id INNER JOIN cities ON stations.city_id = cities.id WHERE cities.province = 'WIELKOPOLSKIE'",
                                con=engine)
sens_w = list(sensors_wielkopol.id)
""" Downloads data for each sensor from the list. """
for s in sens_w:
    data_wielk = load_s(s)
""" Saves them into table air_data. """
data_wielk.to_sql('air_data',
                  engine,
                  schema='public',
                  if_exists='append',
                  index=False)
