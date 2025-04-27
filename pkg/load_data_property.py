import streamlit as st # added
from google.oauth2 import service_account #added
import pandas_gbq # added

@st.cache_resource
def connect_to_data_manhattan(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude,
            land_square_feet,
            building_class_category
    FROM `{table}`
    WHERE UPPER(borough)='MANHATTAN' or borough='1'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_data_bronx(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude,
            land_square_feet,
            building_class_category
    FROM `{table}`
    WHERE UPPER(borough)='BRONX' or borough='2'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_data_brooklyn(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude,
            land_square_feet,
            building_class_category
    FROM `{table}`
    WHERE UPPER(borough)='BROOKLYN' or borough='3'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_data_queens(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude,
            land_square_feet,
            building_class_category
    FROM `{table}`
    WHERE UPPER(borough)='QUEENS' or borough='4'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_data_staten(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT borough, 
            sale_price,
            sale_date,
            latitude,
            longitude,
            land_square_feet,
            building_class_category
    FROM `{table}`
    WHERE UPPER(borough)='STATEN ISLAND' or borough='5'
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)