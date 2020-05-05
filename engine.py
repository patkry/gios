import psycopg2
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

""" Engine to connect python to postgresql database for this project - gios1, via psycopg2. """

engine = create_engine('postgresql+psycopg2://patrycja:patrycja74@/gios1')


def pd_query(sql_guery):
    """ Connects to db gios1, reads to DataFrame given sql query (param: sql_query). """
    q_result = pd.read_sql(sql_guery, con=engine)
    return q_result

if __name__ == "__main__":

    sql_q = """SELECT name
    FROM city 
    WHERE province = 'WIELKOPOLSKIE';"""
    test = pd_query(sql_q)
    print(test)