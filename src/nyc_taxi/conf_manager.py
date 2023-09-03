import os
from pathlib import Path
from dotenv import load_dotenv

PARENT_DIR = os.path.join(Path().absolute(),'src')


load_dotenv()
conf = os.getenv
DATA_URL = conf("DATA_URL")
DOWNLOADS_PATH = os.path.join(PARENT_DIR, 'raw')
STAGING_PATH = os.path.join(PARENT_DIR, 'staging')
CSV_PATH = os.path.join(DOWNLOADS_PATH, 'data.csv')

# Database configuration settings
MAIN_DB = conf("MAIN_DB")
DATABASE = conf("DATABASE")
DB_USER = conf("DB_USER")
DB_PASSWORD = conf("DB_PASSWORD")
HOST = conf("HOST")
PORT = conf("PORT")

if __name__ == "__main__":
    print(PARENT_DIR)