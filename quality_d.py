import json, requests
import pandas as pd
from pandas.io.json import json_normalize

def load_q(s):
    url = 'https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/' + str(s)
    request = requests.get(url)
    q_all=json.loads(request.text)
    lis = ['id','stCalcDate','stIndexLevel']
    q_data1={}
    for l in lis:
        z={l:q_all[l]}
        q_data1.update(z)
    q_data=pd.DataFrame(json_normalize(q_data1))
    q_data.columns = ['station_id','date_q', 'level_id', 'level_name']
    return q_data


if __name__ == "__main__":
    s=52
    q_data=load_q(s)
    print(q_data)