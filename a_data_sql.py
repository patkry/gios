import json, requests
import pandas as pd
from pandas.io.json import json_normalize

from engine import engine
from air_data import load_s

sensors_wielkopol = pd.read_sql("SELECT cities.c_name, sensors.id FROM sensors INNER JOIN stations ON sensors.station_id = stations.id INNER JOIN cities ON stations.city_id = cities.id WHERE cities.province = 'WIELKOPOLSKIE'",
                                con=engine)
sens_w = list(sensors_wielkopol.id)
for s in sens_w:
    data_wielk = load_s(s)

    data_wielk.to_sql('air_data',
                    engine,
                    schema='public', 
                    if_exists='append',
                    index=False)