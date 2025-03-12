#import pandas as pd
import streamlit as st
import sodapy as sodapy

# from sodapy import Socrata
from construction_functions import connect_to_nyc_data, filter_to_new_buildings

all_results_df = connect_to_nyc_data("w9ak-ipjd", "filing_date>'2023-12-31T00:00:00.000'")

new_buildings_permitted = filter_to_new_buildings(all_results_df)


job_type_colors = {
    "Alteration": "#FF0000", # red 
    "Alteration CO": "#FF0000", #red
    "ALT-CO - New Building with Existing Elements to Remain": "#FF0000", # red 
    "No Work": "#00FF00", #green
    "New Building": "#0000FF", # blue New Construction
    "Full Demolition": "#FFA500", #orange - Full Demolition
}

building_type_colors = {
    'Other': '#FF0000', #red
    '3 Family': '#00FF00', #green
    '2 Family': '#FFA500', #orange
    '1 Family': '#0000FF', #blue
}

new_buildings_permitted['color'] = new_buildings_permitted['building_type'].map(building_type_colors).fillna("#808080")


sum_of_new_builds_2024 = len(all_results_df[(all_results_df['filing_date']< '2025-01-01') & (all_results_df['job_type'] == 'New Building')])
sum_of_new_builds_2025 = len(all_results_df[(all_results_df['filing_date']> '2024-12-31') & (all_results_df['job_type'] == 'New Building')])
sum_of_new_units_2024 = new_buildings_permitted[new_buildings_permitted['filing_date']<'2025-01-01']['proposed_dwelling_units'].sum()
sum_of_new_units_2025 = new_buildings_permitted[new_buildings_permitted['filing_date']>'2024-12-31']['proposed_dwelling_units'].sum()

st.title("New Construction Mapping")
st.write("This mapping shows the permitted applications for new building construction throughout New York City from Jan. 2024.")

col1, col2 = st.columns(2) 

with col1:

    with st.container():
        st.metric(label="Number of New Building Applications - 2024",value=sum_of_new_builds_2024,border=True)

    with st.container():
        st.metric(label="Number of New Building Applications - 2025",value=sum_of_new_builds_2025,border=True)

    with st.container():
        st.metric(label="Number of New Permitted Units - 2024",value=sum_of_new_units_2024,border=True)
    
    with st.container():
        st.metric(label="Number of New Permitted Units - 2025",value=sum_of_new_units_2025,border=True)

with col2:
    st.write("New Buildings Permitted Between '24-'25")
    st.map(new_buildings_permitted, latitude='latitude', longitude='longitude',size='proposed_dwelling_units', color='color') 
    '''
    The size of the dots is based on the number of proposed units for each project. 

    The colors are based on the building type: 

    Red dots are classified as "Other", these include anything above a 3-Family Home.  
    Green dots are "3 Family" homes.  
    Orange dots are "2 Family" homes.  
    Blue dots are "1 Family" homes.
    '''








