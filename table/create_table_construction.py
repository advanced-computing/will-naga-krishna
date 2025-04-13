import pandas_gbq
from sodapy import Socrata
import pandas as pd

project_id = "sipa-adv-c-naga-will"
table_id = 'nyc_construction_property.construction_applications'

client = Socrata("data.cityofnewyork.us", None)
df_list = []
offset=0
filter = (
    "filing_date>'2024-12-31T00:00:00.000' OR (filing_date<='2024-12-31T00:00:00.000' AND filing_date>'2023-12-31T00:00:00.000')"
)

while True:
    
    results = client.get('w9ak-ipjd', 
                         where=filter, 
                         limit=5000,
                         offset=offset)
    offset = offset + 5000
    print(len(results), offset)

    if len(results)==0:
        break

    df_list.extend(results)

# data frame
df_construction = pd.DataFrame.from_dict(df_list)

# extract necessary columns
df_construction = df_construction[
      ['job_filing_number',
       'filing_status',
       'borough',
       'building_type',
       'proposed_no_of_stories',
       'proposed_height',
       'proposed_dwelling_units',
       'filing_date',
       'latitude',
       'longitude',
       'job_type']
       ]

# make a table
pandas_gbq.to_gbq(df_construction,
                  table_id,
                  project_id=project_id,
                  if_exists='replace')