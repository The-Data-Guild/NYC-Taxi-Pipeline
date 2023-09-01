import os
import pickle
import pandas as pd
from conf_manager import CSV_PATH, CLEAN_DATA_PATH

def create_datetime_dim(df):
    """function maps data to datetime_dim table

    returns a dictionary"""
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    datetime_dim =df[['tpep_pickup_datetime', 'tpep_dropoff_datetime']].drop_duplicates().reset_index(drop=True)
    datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
    datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
    datetime_dim['pick_weekday'] = datetime_dim['tpep_pickup_datetime'].dt.weekday

    datetime_dim['drop_hour'] = datetime_dim['tpep_dropoff_datetime'].dt.hour
    datetime_dim['drop_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
    datetime_dim['drop_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
    datetime_dim['drop_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year
    datetime_dim['drop_weekday'] = datetime_dim['tpep_dropoff_datetime'].dt.weekday

    datetime_dim['datetime_id'] = datetime_dim.index
    datetime_dim = datetime_dim[['datetime_id', 'tpep_pickup_datetime', 'pick_hour',
                                 'pick_day', 'pick_month', 'pick_year', 'pick_weekday',
                                 'tpep_dropoff_datetime', 'drop_hour', 'drop_day', 'drop_month',
                                 'drop_year', 'drop_weekday']]

    return datetime_dim

def create_passenger_count_dim(df):
    """function maps data to passenger_count_dim table"""
    passenger_count_dim = df[['passenger_count']].drop_duplicates().reset_index(drop=True)
    passenger_count_dim['passenger_count_id'] = passenger_count_dim.index
    passenger_count_dim = passenger_count_dim[['passenger_count_id', 'passenger_count']]

    return  passenger_count_dim

def create_trip_distance_dim(df):
    """function maps data to trip_distance_dim table"""

    trip_distance_dim = df[['trip_distance']].drop_duplicates().reset_index(drop=True)
    trip_distance_dim['trip_distance_id'] = trip_distance_dim.index
    trip_distance_dim = trip_distance_dim[['trip_distance_id', 'trip_distance']]
    return trip_distance_dim

def create_rate_code_dim(df):
    """maps data to rate_code_dim table"""
    rate_code_type = {
        1:"Standard rate",
        2:"JFK",
        3:"Newark",
        4:"Nassau or Westchester",
        5:"Negotiated fare",
        6:"Group ride"
    }

    rate_code_dim = df[['RatecodeID']].drop_duplicates().reset_index(drop=True)
    rate_code_dim['rate_code_id'] = rate_code_dim.index
    rate_code_dim['rate_code_name'] = rate_code_dim['RatecodeID'].map(rate_code_type)
    rate_code_dim = rate_code_dim[['rate_code_id', 'RatecodeID', 'rate_code_name']]
    return rate_code_dim

def transformations(csv):
    """function to transform data"""
    df = pd.read_csv(csv)

    data_dict = create_datetime_dim(df)

    return data_dict


if __name__ == '__main__':
    with open(f"{os.path.join(CLEAN_DATA_PATH, 'data.pickle')}", 'wb') as output:
        pickle.dump(transformations(CSV_PATH), output, pickle.HIGHEST_PROTOCOL)


