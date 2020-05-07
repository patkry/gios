""" Downloads air quality data from GIOS API and saves them in table quality. """

import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

from engine import engine
from quality_d import load_q

""" List of stations ids for api request. """
stat_all = pd.read_sql("SELECT id FROM stations",
                       con=engine)
stat_l = list(stat_all.id)
""" Downloads data from api for every station id. """
for s in stat_l:
    quality = load_q(s)
    """ Saves data to postgresql table. """
    quality.to_sql('quality',
                   engine,
                   schema='public',
                   if_exists='append',
                   index=False)
