import pandas_gbq
from sodapy import Socrata
import pandas as pd
# from pkg.load_data import connect_to_nyc_data

project_id = "sipa-adv-c-naga-will"
table_id = 'nyc_construction_property.property_price'

# load data
# df_land = connect_to_nyc_data('w2pb-icbu', "sale_date>'2020-01-01T00:00:00.000'")

client = Socrata("data.cityofnewyork.us", None)
df_list = []
offset=0
filter = "sale_date>='2022-01-01T00:00:00.000' AND sale_date<'2023-01-01T00:00:00.000'"

while True:
    
    results = client.get('w2pb-icbu', 
                         where=filter, 
                         limit=5000,
                         offset=offset)
    offset = offset + 5000
    print(len(results), offset)

    if len(results)==0:
        break

    df_list.extend(results)

# data frame
# df_land = connect_to_nyc_data('w2pb-icbu', "sale_date>'2020-01-01T00:00:00.000'")
df_land = pd.DataFrame.from_dict(df_list)

# extract necessary columns
df_land = df_land[
      ['borough',
       'neighborhood', 
       'building_class_category', 
       'zip_code',
       'land_square_feet',
       'gross_square_feet',
       'year_built',
       'sale_price',
       'sale_date',
       'latitude',
       'longitude']
       ]

# make a table
pandas_gbq.to_gbq(df_land,
                  table_id,
                  project_id=project_id,
                  if_exists='replace')