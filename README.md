Playing around with some data from gios api (air quality monitoring stations).
This part is about stations data - location, supported parameters.
My goal was to download data, designe database for it, and place data into database.

So we have:
- rest api
- python, pandas, sqlalchemy, psycopg2,
- postgresql.

-----------------

- gios_stations.py and gios_sensors.py - downloads data from api, processes and creates pandas df
- engine.py - creates engine to connect python with postgresql
- stations_tables.py - creates tables for data in database
- stations_tosql.py - sends data to the database
