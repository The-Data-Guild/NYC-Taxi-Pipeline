"""
filename: extract_data.py
Module downloads uber taxi data.csv and writes a copy to raw folder
by Ali Shaheed
"""

import os
from io import StringIO
import requests
import pandas as pd
from conf_manager import DATA_URL, DOWNLOADS_PATH #pylint: disable=import-error

def extract(data, filename):
    """function to download the csv"""
    response = requests.get(data, timeout=10)
    taxi_df = pd.read_csv(StringIO(response.text))
    taxi_df.to_csv(os.path.join(DOWNLOADS_PATH, f'{filename}.csv'), index=False)
    return True


if __name__ == '__main__':
    extract(DATA_URL, 'data')
