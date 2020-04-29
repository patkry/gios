import json, requests
import pandas as pd
from pandas.io.json import json_normalize

request = requests.get('https://api.gios.gov.pl/pjp-api/rest/station/findAll')

# zamiana obiektu na json i praca z zagniezdzonymi slownikami
j_data = json.loads(request.text)
jn_data = json_normalize(j_data)

# df z danymi stacji pomiarowych
stations = jn_data[['id','stationName','gegrLat','gegrLon','city.id','addressStreet']]
stations.columns = ['id','st_name','gegr_lat','gegr_lon','city_id','street']

# df z miastami
cities = jn_data[['city.id','city.name','city.commune.communeName','city.commune.districtName','city.commune.provinceName']].drop_duplicates()
cities.columns = ['id','c_name','commune','district','province']

if __name__ == "__main__":
    print(stations.head())
    print(cities.head())
