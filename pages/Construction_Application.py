import pandas as pd
import streamlit as st
import sodapy as sodapy

# from sodapy import Socrata
from construction_functions import connect_to_nyc_data, remove_blanks, convert_column_to_int, convert_to_float

all_results_df = connect_to_nyc_data("w9ak-ipjd", "filing_date>'2023-12-31T00:00:00.000'")
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

# all_results = []
# offset=0
# while True:
#     client = Socrata("data.cityofnewyork.us", None)
#     results = client.get("ic3t-wcy2", where="job_status='R'", limit=20000,offset=offset)
#     offset = offset + 20000
#     print(len(results),offset)
#     all_results.extend(results)
#     #adding in throttle below for testing
#     if offset >20000:
#     #if len(results)<50000:
#         break
# all_results_df = pd.DataFrame.from_dict(all_results)


trimmed_df = all_results_df[['job_filing_number',
                             'filing_status',
                             'borough',
                             'house_no',
                             'street_name',
                             'initial_cost',
                             'building_type',
                             'existing_stories',
                             'existing_height',
                             'existing_dwelling_units',
                             'proposed_no_of_stories',
                             'proposed_height',
                             'proposed_dwelling_units',
                             'filing_date',
                             'current_status_date',
                             'first_permit_date',
                             'latitude',
                             'longitude',
                             'job_type']]


#create a function to remove blank rows
# def remove_blanks(df, columns):
#     return df[df[columns].notna().all(axis=1)]

#apply function
no_blanks_df = remove_blanks(trimmed_df,['existing_dwelling_units','proposed_dwelling_units'])
#no_blanks_df = trimmed_df[(trimmed_df['gis_latitude'].notna()) & (trimmed_df['proposed_dwelling_units'].notna())]

no_blanks_df = convert_column_to_int(no_blanks_df,['existing_dwelling_units','proposed_dwelling_units'])

 #From ChatGPT: https://chatgpt.com/share/67b36169-fbe0-8009-9e36-14fec4fa4648
# # Convert 'proposed_dwelling_units' to numeric, forcing errors to NaN
# no_blanks_df['proposed_dwelling_units'] = pd.to_numeric(no_blanks_df['proposed_dwelling_units'], errors='coerce')

 # Drop any rows where 'proposed_dwelling_units' became NaN due to invalid conversion
# no_blanks_df = no_blanks_df.dropna(subset=['proposed_dwelling_units'])
 #End segment from ChatGPT

#create a function to convert to float
# def convert_to_float(df, columns):
#     df[columns] = df[columns].astype(float)
#     return df
#apply function
no_blanks_df = convert_to_float(no_blanks_df, ['latitude','longitude'])

#no_blanks_df['gis_latitude']= no_blanks_df['gis_latitude'].astype(float)
#no_blanks_df['gis_longitude'] = no_blanks_df['gis_longitude'].astype(float)
# no_blanks_df['proposed_dwelling_units'] = no_blanks_df['proposed_dwelling_units'].astype(int)

no_blanks_df['filing_date'] = pd.to_datetime(no_blanks_df['filing_date'],format='mixed')


# last_two_years = no_blanks_df[no_blanks_df['pre__filing_date']>'2023-01-01']
#adding colors to the job types - taken from Naga's code, assisted by ChatGPT
job_type_colors = {
    "Alteration": "#FF0000", # red 
    "Alteration CO": "#FF0000", #red
    "ALT-CO - New Building with Existing Elements to Remain": "FF0000", # red 
    "No Work": "#00FF00", #green
    "New Building": "#0000FF", # blue New Construction
    "Full Demolition": "#FFA500", #orange - Full Demolition
}


no_blanks_df['color'] = no_blanks_df['job_type'].map(job_type_colors).fillna("#808080")

# New column for change in units -- put that in the size? (negative values?)
# FILTER DOWN TO 2025 -- put the sums for change in units and rows

st.title("NYC Construction Applications Mapping")
st.write("This mapping shows the approved applications for construction throughout New York City from Jan. 2023 to today.")
st.map(no_blanks_df, latitude='latitude', longitude='longitude',size='proposed_dwelling_units',color='color')

'''
The size of the dots is based on the number of proposed units for each project.
The colors are based on the construction type.
Red dots are projects for Alteration Type 1 (A1) which are considered major changes that require a new Certificate of Occupany.
Green dots are for Alteration Type 2 (A2) which are considered minor interior renovations that do not require a new Certificate of Occupancy.
Orange dots are for Alteration Type 3 (A3) which are considered minor renovations typically to the exterior like fences.
Blue dots are for New Building (NB) construction
'''