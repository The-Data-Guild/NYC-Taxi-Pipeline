"""
filename:provision_database.py
Module creates and sets up database ready for data to be loaded
by Ali Shaheed
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from conf_manager import DB_USER, DB_PASSWORD, HOST, PORT, DATABASE, MAIN_DB #pylint: disable=import-error

# create db connection
def db_connect(db):
    """function to create db connection"""
    connection = psycopg2.connect(database=db,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        host=HOST,
                        port=PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return connection

# create database
def create_db(connection):
    """function to create db"""
    with connection.cursor() as curs:
        curs.execute(f"CREATE DATABASE {DATABASE};")
        print(f"Database {DATABASE} created.")
    return True

if __name__ == '__main__':
    con = db_connect(MAIN_DB)
    # create database
    create_db(con)