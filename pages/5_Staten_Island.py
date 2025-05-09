# import libraries
import streamlit as st
from pkg.mapping import pydeck_chart
from pkg.property_functions import to_float
from pkg.load_data_property import connect_to_data_staten
from pkg.load_data_construction import connect_to_bigquery_staten
from pkg.construction_functions import filter_to_new_buildings
# title
st.title("Staten Island")

# Takeaways
st.markdown('''
            - Staten Island tends to look much more like a typical suburb compared to the rest of NYC so it's not surprising that the development are mostly 1-2 family homes.
            - The prices of sold properties are the lowest among the NYC boroughs.
            - It may be worth exploring why the multi-family development is concentrated on the New Jersey side of the island.
            ''')

tab1, tab2 = st.tabs(["Construction Applications", "Property Price"])

with tab1:
    st.markdown("Permitted Applications for New Building Construction from January 2024")

    # construnction –> Will Part
    table='sipa-adv-c-naga-will.nyc_construction_property.construction_applications'
    df_construction = connect_to_bigquery_staten(table)
    new_buildings_permitted = filter_to_new_buildings(df_construction)

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

    sum_of_new_builds_2024 = len(df_construction[(df_construction['filing_date']< '2025-01-01') & (df_construction['job_type'] == 'New Building')])
    sum_of_new_builds_2025 = len(df_construction[(df_construction['filing_date']> '2024-12-31') & (df_construction['job_type'] == 'New Building')])
    sum_of_new_units_2024 = new_buildings_permitted[new_buildings_permitted['filing_date']<'2025-01-01']['proposed_dwelling_units'].sum()
    sum_of_new_units_2025 = new_buildings_permitted[new_buildings_permitted['filing_date']>'2024-12-31']['proposed_dwelling_units'].sum()

    # create a dashboard
    st.write("")
    col1, col2 = st.columns(2) 
    col3, = st.columns(1)

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
        st.map(new_buildings_permitted, 
            latitude='latitude', 
            longitude='longitude', 
            size='proposed_dwelling_units', 
            color='color') 
        
    with col3:
        st.write('''
        - The size of the dots is based on the number of proposed units for each project. 
        - The colors are based on the building type: 
            - 🟥 **Red**: Other (4+ Family or Commercial)
            - 🟩 **Green**: 3 Family
            - 🟧 **Orange**: 2 Family
            - 🟦 **Blue**: 1 Family
        ''')

with tab2:
    st.markdown("Prices of Sold Properties in 2022")

    # prorty price –> Naga Part

    # load data
    table='sipa-adv-c-naga-will.nyc_construction_property.property_price'
    df_land = connect_to_data_staten(table)

    # transform data into float
    df_land['sale_price'] = to_float(df_land['sale_price'])
    df_land['land_square_feet'] = to_float(df_land['land_square_feet'])
    df_land['latitude'] = to_float(df_land['latitude'])
    df_land['longitude'] = to_float(df_land['longitude'])
    df_land = df_land[(df_land["sale_price"] > 0) & (df_land["land_square_feet"] > 0)]

    # number of sold properties
    num = len(df_land)

    # avg price of sold properties
    avg = df_land['sale_price'].mean()

    # maximum price of sold properties
    max = df_land['sale_price'].max()

    # average price of sold properties per square foot
    avg_per_sf = (df_land['sale_price']/df_land['land_square_feet']).mean()

    # delete the rows including 'Nan'
    df_land.dropna(subset=["latitude", "longitude", "sale_price"], inplace=True)

    # create a dashboard
    st.write("")
    col1, col2 = st.columns(2) 
    col3, = st.columns(1)

    with col1:
        with st.container():
            st.metric("The number of sold properties", f"{num:,.0f}", border=True)

        with st.container():
            st.metric("The average price of sold properties", f"${avg:,.0f}", border=True)

        with st.container():
            st.metric("The maximum price of sold properties", f"${max:,.0f}", border=True)
        
        with st.container():
            st.metric("The average price of sold properties per land sf", f"${avg_per_sf:,.0f}", border=True)

    with col2:
        pydeck_chart(df_land, "staten")

    with col3:
        st.write('''
        - The height of the dots in the map is based on the relative prices of sold properties per land square foot. 
        - The colors are based on the building type: 
            - 🟥 **Red**: Other (4+ Family or Commercial)
            - 🟩 **Green**: 3 Family
            - 🟧 **Orange**: 2 Family
            - 🟦 **Blue**: 1 Family
                 ''')