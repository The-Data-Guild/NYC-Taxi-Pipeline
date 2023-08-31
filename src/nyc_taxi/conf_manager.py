import os
from pathlib import Path
from dotenv import load_dotenv

PARENT_DIR = Path().absolute().parent

load_dotenv()
conf = os.getenv
DATA_URL = conf("DATA_URL")
DOWNLOADS_PATH = os.path.join(PARENT_DIR, 'raw')

if __name__ == "__main__":
    print(DATA_URL)