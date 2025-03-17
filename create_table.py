import pandas_gbq
from pkg.load_data import connect_to_nyc_data

project_id = "sipa-adv-c-naga-will"
table_id = 'nyc_construction_property.property_price'

# load data
df_land = connect_to_nyc_data('w2pb-icbu', "sale_date>'2020-01-01T00:00:00.000'")

pandas_gbq.to_gbq(df_land, table_id, project_id=project_id)