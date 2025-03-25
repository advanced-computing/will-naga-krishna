import pandas_gbq
# from sodapy import Socrata
# import pandas as pd
# from pkg.load_data import connect_to_nyc_data
from pkg.construction_functions import connect_to_nyc_data, filter_to_new_buildings

project_id = "sipa-adv-c-naga-will"
table_id = 'nyc_construction_property.construction_applications'

# from sodapy import Socrata


all_results_df = connect_to_nyc_data("w9ak-ipjd", "filing_date>'2023-12-31T00:00:00.000'")

new_buildings_permitted = filter_to_new_buildings(all_results_df)


# make a table
pandas_gbq.to_gbq(new_buildings_permitted,
                  table_id,
                  project_id=project_id,
                  if_exists='replace')