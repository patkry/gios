""" Creating DataFrame for a specific sensor from data downloaded from api. """

import json, requests
import pandas as pd
from pandas.io.json import json_normalize

def load_s(z):
    """ Creates url with sensor id as function argument, downloads data from api, parse json to python dictionary, flattens  it, constructs DataFrame and changes columns in it for data base table 'air_data'"""
    url = 'https://api.gios.gov.pl/pjp-api/rest/data/getData/' + str(z)
    request = requests.get(url)
    sensor_d=pd.DataFrame(json_normalize(json.loads(request.text),'values'))
    sensor_d['id']=z
    cols = sensor_d.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    sensor_d=sensor_d[cols]
    sensor_d.columns = ['sensor_id','date_s','sensor_v']
    return sensor_d

if __name__ == "__main__":
    k=92
    sensor_data=load_s(k)
    print(sensor_data.head())