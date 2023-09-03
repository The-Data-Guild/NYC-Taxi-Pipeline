import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from conf_manager import DB_USER, DB_PASSWORD, HOST, PORT, DATABASE, DB_PATH, TABLESPACE, MAIN_DB

conn = psycopg2.connect(database=MAIN_DB,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        host=HOST,
                        port=PORT)


conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

with conn.cursor() as curs:
    curs.execute(sql.SQL("CREATE TABLESPACE {tablespace} LOCATION {db_path};")
                 .format(tablespace = sql.Identifier(TABLESPACE),
                         db_path = sql.Literal(DB_PATH)))
    curs.execute(f"CREATE DATABASE {DATABASE};")
    print(f"Database {DATABASE} SET TABLESPACE '{DB_PATH}'")
