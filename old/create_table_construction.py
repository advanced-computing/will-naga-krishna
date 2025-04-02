import pandas_gbq
# from sodapy import Socrata
# import pandas as pd
# from pkg.load_data import connect_to_nyc_data
from pkg.construction_functions import connect_to_nyc_data
from google.cloud import bigquery

project_id = "sipa-adv-c-naga-will"
table_id = 'nyc_construction_property.construction_applications'
client = bigquery.Client(project=project_id)
# from sodapy import Socrata

# Get the most recent filing_date from BigQuery
def get_latest_filing_date():
    query = f"SELECT MAX(filing_date) AS latest_filing_date FROM `{project_id}.{table_id}`"
    result = client.query(query).to_dataframe()
    return result['latest_filing_date'][0] or '2023-12-31T00:00:00.000'

latest_filing_date = get_latest_filing_date()

all_results_df = connect_to_nyc_data("w9ak-ipjd", f"filing_date>'{latest_filing_date}'")

if not all_results_df.empty:
    pandas_gbq.to_gbq(all_results_df, table_id, project_id=project_id, if_exists='append')
    print("New data appended successfully.")
else:
    print("No new data to append.")

# all_results_df = connect_to_nyc_data("w9ak-ipjd", "filing_date>'2023-12-31T00:00:00.000'")

# # new_buildings_permitted = filter_to_new_buildings(all_results_df)

# #print(all_results_df.shape)
# # print(new_buildings_permitted.shape)

# # make a table
# pandas_gbq.to_gbq(all_results_df,
#                   table_id,
#                   project_id=project_id,
#                   if_exists='replace')