import os
from pathlib import Path
from dotenv import load_dotenv

PARENT_DIR = os.path.join(Path().absolute(),'src')


load_dotenv()
conf = os.getenv
DATA_URL = conf("DATA_URL")
DOWNLOADS_PATH = os.path.join(PARENT_DIR, 'raw')
CLEAN_DATA_PATH = os.path.join(PARENT_DIR, 'clean')
CSV_PATH = os.path.join(DOWNLOADS_PATH, 'data.csv')

# Database configuration settings
DB_PATH = os.path.join(PARENT_DIR, 'data')
MAIN_DB = conf("MAIN_DB")
DATABASE = conf("DATABASE")
TABLESPACE = f"{DATABASE}_space"
DB_USER = conf("DB_USER")
DB_PASSWORD = conf("DB_PASSWORD")
HOST = conf("HOST")
PORT = conf("PORT")

if __name__ == "__main__":
    print(PARENT_DIR)
    print(DB_PATH) # should print the url of where the data is being downloaded from