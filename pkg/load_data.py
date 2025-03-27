import streamlit as st # added
from google.oauth2 import service_account #added
import pandas_gbq # added

#def connect_to_nyc_data(table, borough):

#     # create API client
#     creds = st.secrets["gcp_service_account"]
#     credentials = service_account.Credentials.from_service_account_info(creds)

#     # filter_datetime = f"""
#     # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
#     # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
#     # """

#     sql = f"""
#     SELECT borough, 
#             sale_price,
#             sale_date,
#             latitude,
#             longitude
#     FROM `{table}`
#     WHERE borough = '{borough}'
#     """

#     return pandas_gbq.read_gbq(sql, credentials=credentials)

def connect_to_data_manhattan(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude
    FROM `{table}`
    WHERE UPPER(borough)='MANHATTAN' or borough='1'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

def connect_to_data_bronx(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude
    FROM `{table}`
    WHERE UPPER(borough)='BRONX' or borough='2'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

def connect_to_data_brooklyn(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude
    FROM `{table}`
    WHERE UPPER(borough)='BROOKLYN' or borough='3'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

def connect_to_data_queens(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude
    FROM `{table}`
    WHERE UPPER(borough)='QUEENS' or borough='4'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

def connect_to_data_staten(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude
    FROM `{table}`
    WHERE UPPER(borough)='STATEN ISLAND' or borough='5'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)