import os
from pathlib import Path
from dotenv import load_dotenv

PARENT_DIR = Path().absolute().parent

load_dotenv()
conf = os.getenv
DATA_URL = conf("DATA_URL")
DOWNLOADS_PATH = os.path.join(PARENT_DIR, 'raw')
CLEAN_DATA_PATH = os.path.join(PARENT_DIR, 'clean')
CSV_PATH = os.path.join(DOWNLOADS_PATH, 'data.csv')

if __name__ == "__main__":
    print(DATA_URL) # should print the url of where the data is being downloaded from