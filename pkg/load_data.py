import streamlit as st # added
from google.oauth2 import service_account #added
import pandas_gbq # added

def connect_to_nyc_data(table):

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
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

# def connect_to_nyc_data(api_code, filter):

#     all_results = []
#     offset=0

#     while True:
#         client = Socrata("data.cityofnewyork.us", None)
#         results = client.get(api_code, 
#                              where=filter, 
#                              limit=50000,
#                              offset=offset)
#         offset = offset + 50000
#         print(len(results), offset)
#         all_results.extend(results)

#         if len(results)<50000:
#             break

#     return pd.DataFrame.from_dict(all_results)