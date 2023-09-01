"""
filename: data_transformations.py
Module maps data for db schema

Returns *.pickle file
by Ali Shaheed
"""
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

def create_pickup_location_dim(df):
    """function maps data to pickup_location_dim table"""
    pickup_location_dim = df[['pickup_longitude', 'pickup_latitude']].drop_duplicates().reset_index(drop=True)
    pickup_location_dim['pickup_location_id'] = pickup_location_dim.index
    pickup_location_dim = pickup_location_dim[['pickup_location_id', 'pickup_longitude', 'pickup_latitude']]
    return pickup_location_dim

def create_dropoff_location_dim(df):
    """function maps data to dropoff_location_dim table"""
    dropoff_location_dim = df[['dropoff_longitude', 'dropoff_latitude']].drop_duplicates().reset_index(drop=True)
    dropoff_location_dim['dropoff_location_id'] = dropoff_location_dim.index
    dropoff_location_dim = dropoff_location_dim[['dropoff_location_id', 'dropoff_longitude', 'dropoff_latitude']]
    return dropoff_location_dim

def create_payment_type_dim(df):
    """function maps data to payment_type_dim table"""
    payment_type_name = {
        1:"Credit card",
        2:"Cash",
        3:"No charge",
        4:"Dispute",
        5:"Unknown",
        6:"Voided trip"
    }

    payment_type_dim = df[['payment_type']].drop_duplicates().reset_index(drop=True)
    payment_type_dim['payment_type_id'] = payment_type_dim.index
    payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(payment_type_name)
    payment_type_dim = payment_type_dim[['payment_type_id', 'payment_type', 'payment_type_name']]
    return payment_type_dim

def create_fact_table(df, passenger_count, trip_distance, rate_code, pickup_location,
                      dropoff_location, date_time, payment_type):
    """function maps data to fact_table"""
    face_table = df.merge(passenger_count, on='passenger_count') \
            .merge(trip_distance, on='trip_distance') \
            .merge(rate_code, on='RatecodeID') \
            .merge(pickup_location, on=['pickup_longitude', 'pickup_latitude']) \
            .merge(dropoff_location, on=['dropoff_longitude', 'dropoff_latitude']) \
            .merge(date_time, on=['tpep_pickup_datetime', 'tpep_dropoff_datetime']) \
            .merge(payment_type, on='payment_type') \
            [['VendorID', 'datetime_id', 'passenger_count_id', 'trip_distance_id',
              'rate_code_id', 'store_and_fwd_flag', 'pickup_location_id', 'dropoff_location_id',
              'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
              'improvement_surcharge', 'total_amount']]
    return face_table

def transformations(csv):
    """function to transform data mapping it to db schema"""
    df = pd.read_csv(csv)
    datetime_dim = create_datetime_dim(df)
    passenger_count_dim = create_passenger_count_dim(df)
    trip_distance_dim = create_trip_distance_dim(df)
    rate_code_dim = create_rate_code_dim(df)
    pickup_location_dim = create_pickup_location_dim(df)
    dropoff_location_dim = create_dropoff_location_dim(df)
    payment_type_dim = create_payment_type_dim(df)
    fact_table = create_fact_table(df, passenger_count_dim, trip_distance_dim, rate_code_dim, pickup_location_dim,
                                   dropoff_location_dim, datetime_dim, payment_type_dim)

    data_dict = {
        "datetime_dim:":datetime_dim,
        "passenger_count_dim":passenger_count_dim,
        "trip_distance_dim":trip_distance_dim,
        "rate_code_dim":rate_code_dim,
        "pickup_location_dim":pickup_location_dim,
        "dropoff_location_dim":dropoff_location_dim,
        "payment_type_dim":payment_type_dim,
        "fact_table":fact_table
    }

    return data_dict


if __name__ == '__main__':
    with open(f"{os.path.join(CLEAN_DATA_PATH, 'data.pickle')}", 'wb') as output:
        pickle.dump(transformations(CSV_PATH), output, pickle.HIGHEST_PROTOCOL)
