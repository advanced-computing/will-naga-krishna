import pandas as pd
import streamlit as st
import sodapy as sodapy

# from sodapy import Socrata
from construction_functions import connect_to_nyc_data, remove_blanks, convert_column_to_int, convert_to_float

all_results_df = connect_to_nyc_data("w9ak-ipjd", "filing_date>'2024-12-31T00:00:00.000'")



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



no_blanks_df = remove_blanks(trimmed_df,['existing_dwelling_units','proposed_dwelling_units','latitude','longitude'])


no_blanks_df = convert_column_to_int(no_blanks_df,['existing_dwelling_units','proposed_dwelling_units'])

no_blanks_df = convert_to_float(no_blanks_df, ['latitude','longitude'])


no_blanks_df['filing_date'] = pd.to_datetime(no_blanks_df['filing_date'],format='mixed')
approved_2025 = no_blanks_df[no_blanks_df['filing_status'].isin(['Approved'])]


job_type_colors = {
    "Alteration": "#FF0000", # red 
    "Alteration CO": "#FF0000", #red
    "ALT-CO - New Building with Existing Elements to Remain": "#FF0000", # red 
    "No Work": "#00FF00", #green
    "New Building": "#0000FF", # blue New Construction
    "Full Demolition": "#FFA500", #orange - Full Demolition
}


approved_2025['color'] = approved_2025['job_type'].map(job_type_colors).fillna("#808080")

# New column for change in units -- put that in the size? (negative values?)


st.title("NYC Construction Applications Mapping")
st.write("This mapping shows the approved applications for construction throughout New York City from Jan. 2025 to today.")
st.map(approved_2025, latitude='latitude', longitude='longitude', color='color') #size='proposed_dwelling_units'

'''
The size of the dots is based on the number of proposed units for each project.
The colors are based on the construction type.
Red dots are projects for Alteration Type 1 (A1) which are considered major changes that require a new Certificate of Occupany.
Green dots are for Alteration Type 2 (A2) which are considered minor interior renovations that do not require a new Certificate of Occupancy.
Orange dots are for Alteration Type 3 (A3) which are considered minor renovations typically to the exterior like fences.
Blue dots are for New Building (NB) construction
'''