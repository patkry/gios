import json, requests
import pandas as pd
from pandas.io.json import json_normalize

from engine import engine
from quality_d import load_q

stat_all = pd.read_sql("SELECT id FROM stations",
                                con=engine)
stat_l = list(stat_all.id)
for s in stat_l:
    quality = load_q(s)

    quality.to_sql('quality',
                    engine,
                    schema='public', 
                    if_exists='append',
                    index=False)