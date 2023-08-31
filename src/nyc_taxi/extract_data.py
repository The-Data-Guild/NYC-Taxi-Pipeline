import os
from io import StringIO
import requests
import pandas as pd
from conf_manager import DATA_URL, DOWNLOADS_PATH

def extract(data, filename):
    response = requests.get(data, timeout=10)
    taxi_df = pd.read_csv(StringIO(response.text))
    taxi_df.to_csv(os.path.join(DOWNLOADS_PATH, f'{filename}.csv'), index=False)


if __name__ == '__main__':
    extract(DATA_URL, 'data')