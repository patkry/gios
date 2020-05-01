# silnik do łączenia z bazą postgresql

import psycopg2
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://patrycja:patrycja74@/gios1')

if __name__ == "__main__":
    import pandas as pd
    cities_wielkopol = pd.read_sql("SELECT name FROM city WHERE province = 'WIELKOPOLSKIE'",
                                con=engine)
    print(cities_wielkopol)