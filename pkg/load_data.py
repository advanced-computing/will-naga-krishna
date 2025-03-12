from sodapy import Socrata
import pandas as pd

def connect_to_nyc_data(api_code, filter):

    all_results = []
    offset=0

    while True:
        client = Socrata("data.cityofnewyork.us", None)
        results = client.get(api_code, 
                             where=filter, 
                             limit=50000,
                             offset=offset)
        offset = offset + 50000
        print(len(results), offset)
        all_results.extend(results)

        if len(results)<50000:
            break

    return pd.DataFrame.from_dict(all_results)