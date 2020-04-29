import json, requests
import pandas as pd
from pandas.io.json import json_normalize
from gios_stations import stations

# lista id stacji pomiarowych do zapytania o sensory dostępne dla danej stacji
stat_id = list(stations.id)

# zapytanie tworzące listę sensorów i parametrów dla każdej stacji pomiarowej
sensors_data = []
for s in stat_id:
    url = 'https://api.gios.gov.pl/pjp-api/rest/station/sensors/'+str(s)
    request = requests.get(url)
    j_data = json.loads(request.text)
    for j in j_data:
        sensors_data.append(j)

# obróbka listy do df
data=pd.DataFrame(json_normalize(sensors_data))

# dane sensorow
sensors = data[['id', 'param.idParam', 'stationId']]
sensors.columns = ['id', 'param_id', 'station_id']

# dane parametrów
params = data[["param.idParam",'param.paramCode','param.paramFormula','param.paramName']].drop_duplicates()
params.columns = ['id', 'code', 'formula', 'p_name']

if __name__ == "__main__":
    print(sensors.head())
    print(params.head())