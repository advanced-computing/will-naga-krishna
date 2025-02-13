import pandas as pd
import streamlit as st
import sodapy as sodapy

#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
#! pip install sodapy

from sodapy import Socrata
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# client.timeout = 60

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ic3t-wcy2", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)



trimmed_df = results_df[['job__',
                         'borough',
                         'house__',
                         'street_name',
                         'job_type',
                         'job_status',
                         'building_type',
                         'fully_permitted',
                         'existing_dwelling_units',
                         'proposed_dwelling_units',
                         'existing_occupancy',
                         'proposed_occupancy',
                         'gis_latitude',
                         'gis_longitude']]


no_blanks_df = trimmed_df[trimmed_df['gis_latitude'].notna() & trimmed_df['proposed_dwelling_units'].notna()]



no_blanks_df['gis_latitude']= no_blanks_df['gis_latitude'].astype(float)
no_blanks_df['gis_longitude'] = no_blanks_df['gis_longitude'].astype(float)
no_blanks_df['proposed_dwelling_units'] = no_blanks_df['proposed_dwelling_units'].astype(int)

st.title("NYC Construction Applications Mapping - Will & Naga")
st.write("This is our first attempt at building a map of the construction applications data in Streamlit")
st.map(no_blanks_df, latitude='gis_latitude', longitude='gis_longitude',size='proposed_dwelling_units')