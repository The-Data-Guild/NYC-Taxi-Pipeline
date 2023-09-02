import psycopg2
from conf_manager import DB_USER, DB_PASSWORD, HOST, PORT, DATABASE, DB_PATH, TABLESPACE

conn = psycopg2.connect(database=DATABASE,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        host=HOST,
                        port=PORT)

conn.autocommit = True

with conn.cursor() as curs:
    curs.execute(f"CREATE TABLESPACE {TABLESPACE} LOCATION {DB_PATH};")
    curs.execute(f"CREATE DATABASE {DATABASE};")
    print(f"Database {DATABASE} SET TABLESPACE {DB_PATH}")
