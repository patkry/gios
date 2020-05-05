""" DataFramed SQL querries. """

import pandas as pd

from engine import engine, pd_query

""" List of all measuring stations in Wielkopolska and their parameters. """
w_params = """SELECT c.c_name as city,
st.st_name as station,
p.p_name as parameter
FROM cities c
LEFT JOIN stations st ON c.id=st.city_id
LEFT JOIN sensors s ON st.id=s.station_id
LEFT JOIN params p ON s.param_id=p.id
WHERE c.province = 'WIELKOPOLSKIE';"""
all_wiel_sensors = pd_query(w_params)

""" The number of sensors for each parameter (in the province Wielkopolska). """
p_count = """SELECT p.p_name as parameter, COUNT(p.id) as sensors_count
FROM params p
LEFT JOIN sensors s ON p.id=s.param_id
LEFT JOIN stations st ON s.station_id=st.id
LEFT JOIN cities c ON st.city_id=c.id
WHERE c.province = 'WIELKOPOLSKIE'
GROUP BY p.id
ORDER BY sensors_count DESC;"""
params_in_w = pd_query(p_count)

""" Data from one day, one parameter and all its sensors in the province. """
pm10_d_wiel = """SELECT c.c_name || ' ' || st.street as address, a.date_s as date, a.sensor_v as value
FROM air_data a
LEFT JOIN sensors s ON a.sensor_id=s.id
LEFT JOIN params p ON s.param_id=p.id
LEFT JOIN stations st ON s.station_id=st.id
LEFT JOIN cities c ON st.city_id=c.id
WHERE a.sensor_v IS NOT NULL AND a.date_s BETWEEN '2020-04-29 01:00:00' AND '2020-04-30 01:00:00' AND p.p_name='pył zawieszony PM10';"""
pm10_day_wielk = pd_query(pm10_d_wiel)

if __name__ == "__main__":
    print(pm10_day_wielk.head())