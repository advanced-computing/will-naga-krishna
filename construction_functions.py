import sodapy as sodapy
from sodapy import Socrata
import pandas as pd



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
        client = Socrata("data.cityofnewyork.us", None)
        results = client.get(api_code, where=filter, limit=50000,offset=offset)
        offset = offset + 50000
        print(len(results),offset)
        all_results.extend(results)
        if len(results)<50000:
            break
    return pd.DataFrame.from_dict(all_results)


def remove_blanks(df, columns):
    return df[df[columns].notna().all(axis=1)]


def convert_column_to_int(df,columns):
    for col in columns:
        df[col] = df[col].astype(int)
    return df


def convert_to_float(df, columns):
    df[columns] = df[columns].astype(float)
    return df