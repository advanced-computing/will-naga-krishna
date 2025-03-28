import sodapy as sodapy
from sodapy import Socrata
import pandas as pd
import streamlit as st # added
from google.oauth2 import service_account #added
import pandas_gbq # added

@st.cache_resource
def connect_to_nyc_data(api_code,filter):
        # Unauthenticated client only works with public data sets. Note 'None'
        # in place of application token, and no username or password:
        #client = Socrata("data.cityofnewyork.us", None)

        # Example authenticated client (needed for non-public datasets):
        # client = Socrata(data.cityofnewyork.us,
        #                  MyAppToken,
        #                  username="user@example.com",
        #                  password="AFakePassword")

        # client.timeout = 60

        # First 2000 results, returned as JSON from API / converted to Python list of
        # dictionaries by sodapy.
        #results = client.get("ic3t-wcy2", limit=2000)

        # Convert to pandas DataFrame
        #results_df = pd.DataFrame.from_records(results)

    all_results = []
    offset=0
    while True:
        creds = st.secrets["socrata"]
        client = Socrata("data.cityofnewyork.us",
                         creds["app_token"],
                         username=creds["username"],
                         password=creds["password"]
                         )
        results = client.get(api_code, where=filter, limit=50000,offset=offset)
        offset = offset + 50000
        print(len(results),offset)
        all_results.extend(results)
        #throttling data for now
        # if len(results) < 500000
        if len(all_results) > 100000:
            break
    return pd.DataFrame.from_dict(all_results)

@st.cache_resource
def remove_blanks(df, columns):
    return df[df[columns].notna().all(axis=1)]

@st.cache_resource
def convert_column_to_int(df,columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
    return df

@st.cache_resource
def convert_to_float(df, columns):
    df[columns] = df[columns].astype(float)
    return df

@st.cache_resource
def filter_to_new_buildings(df):

    no_blanks_df = remove_blanks(df,['latitude','longitude'])


    no_blanks_df = convert_column_to_int(no_blanks_df,['proposed_dwelling_units'])

    no_blanks_df = convert_to_float(no_blanks_df, ['latitude','longitude'])


    no_blanks_df['filing_date'] = pd.to_datetime(no_blanks_df['filing_date'],format='mixed')

    permitted = no_blanks_df[no_blanks_df['filing_status'].isin(['Permit Entire','Permit Issued','LOC Issued'])]

    #permitted['change_in_units'] = permitted['proposed_dwelling_units'] - permitted['existing_dwelling_units']

    return permitted[permitted['job_type']== 'New Building']

@st.cache_resource
def connect_to_bigquery(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    # filter_datetime = f"""
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) IS NOT NULL AND
    # SAFE.PARSE_DATETIME('%Y-%m-%dT%H:%M:%S.%f', sale_date) > DATETIME '{filter}'
    # """

    sql = f"""
    SELECT job_filing_number,
            filing_status,
            building_type,
            proposed_no_of_stories,
            proposed_height,
            proposed_dwelling_units,
            filing_date,
            latitude,
            longitude,
            job_type
    FROM `{table}`
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)