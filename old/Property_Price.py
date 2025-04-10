# import libraries
import streamlit as st
from pkg.mapping import pydeck_chart
from pkg.property_functions import to_float, to_borough_name
from pkg.load_data_property import connect_to_nyc_data

# title
st.title("NYC Property Price")
st.title("Will & Naga")

# description
'''
This dashboard shows the prices of properties sold in NYC in 2022.
'''
st.write("")

# load data
table='sipa-adv-c-naga-will.nyc_construction_property.property_price'
# filter='2020-01-01T00:00:00.000'
df_land = connect_to_nyc_data(table)
# df_land = connect_to_nyc_data('w2pb-icbu', "sale_date>'2020-01-01T00:00:00.000'")

# form dataframe
# df_land = df_land[
#       ['borough',
#        'neighborhood', 
#        'building_class_category', 
#        'zip_code',
#        'land_square_feet',
#        'gross_square_feet',
#        'year_built',
#        'sale_price',
#        'sale_date',
#        'latitude',
#        'longitude']
#        ]

# transform data into float
df_land['sale_price'] = to_float(df_land['sale_price'])
df_land['latitude'] = to_float(df_land['latitude'])
df_land['longitude'] = to_float(df_land['longitude'])

# classify the borough
df_land['borough'] = df_land['borough'].apply(to_borough_name)
df_land_manhattan = df_land[df_land['borough']=='Manhattan']
df_land_brooklyn = df_land[df_land['borough']=='Brooklyn']
df_land_queens = df_land[df_land['borough']=='Queens']
df_land_bronx = df_land[df_land['borough']=='Bronx']
df_land_staten = df_land[df_land['borough']=='Staten Island']

# number of sold properties
num_manhattan = len(df_land_manhattan)
num_brooklyn = len(df_land_brooklyn)
num_queens = len(df_land_queens)
num_bronx = len(df_land_bronx)
num_staten = len(df_land_staten)

# avg price of sold properties
avg_manhattan = df_land_manhattan['sale_price'].mean()
avg_brooklyn = df_land_brooklyn['sale_price'].mean()
avg_queens = df_land_queens['sale_price'].mean()
avg_bronx = df_land_bronx['sale_price'].mean()
avg_staten = df_land_staten['sale_price'].mean()

# maximum price of sold properties
max_manhattan = round(df_land_manhattan['sale_price'].max(), 2)
max_brooklyn = round(df_land_brooklyn['sale_price'].max(), 2)
max_queens = round(df_land_queens['sale_price'].max(), 2)
max_bronx = round(df_land_bronx['sale_price'].max(), 2)
max_staten = round(df_land_staten['sale_price'].max(), 2)
# max_manhattan = df_land_manhattan['sale_price'].max().round(2)
# max_brooklyn = df_land_brooklyn['sale_price'].max().round(2)
# max_queens = df_land_queens['sale_price'].max().round(2)
# max_bronx = df_land_bronx['sale_price'].max().round(2)
# max_staten = df_land_staten['sale_price'].max().round(2)

# delete the rows including 'Nan'
df_land.dropna(subset=["latitude", "longitude", "sale_price"], inplace=True)

# create a dashboard

# manhattan

col1, col2 = st.columns(2) 

with col1:
    st.write("Manhattan")

    with st.container():
        st.metric("The number of sold properties", f"{num_manhattan:,.0f}", border=True)

    with st.container():
        st.metric("The average price of sold properties", f"${avg_manhattan:,.0f}", border=True)
    
    with st.container():
        st.metric("The maximum price of sold properties", f"${max_manhattan:,.0f}", border=True)

with col2:
    st.write("3D Map")
    pydeck_chart(df_land_manhattan, "manhattan")

st.write("")

# brooklyn

col1, col2 = st.columns(2) 

with col1:
    st.write("Brooklyn")

    with st.container():
        st.metric("The number of sold properties", f"{num_brooklyn:,.0f}", border=True)

    with st.container():
        st.metric("The average price of sold properties", f"${avg_brooklyn:,.0f}", border=True)
    
    with st.container():
        st.metric("The maximum price of sold properties", f"${max_brooklyn:,.0f}", border=True)

with col2:
    st.write("3D Map")
    pydeck_chart(df_land_brooklyn, "brooklyn")

st.write("")

# queens
col1, col2 = st.columns(2) 

with col1:
    st.write("Queens")

    with st.container():
        st.metric("The number of sold properties", f"{num_queens:,.0f}", border=True)

    with st.container():
        st.metric("The average price of sold properties", f"${avg_queens:,.0f}", border=True)
    
    with st.container():
        st.metric("The maximum price of sold properties", f"${max_queens:,.0f}", border=True)

with col2:
    st.write("3D Map")
    pydeck_chart(df_land_queens, "queens")

st.write("")

# bronx
col1, col2 = st.columns(2) 

with col1:
    st.write("Bronx")

    with st.container():
        st.metric("The number of sold properties", f"{num_bronx:,.0f}", border=True)

    with st.container():
        st.metric("The average price of sold properties", f"${avg_bronx:,.0f}", border=True)
    
    with st.container():
        st.metric("The maximum price of sold properties", f"${max_bronx:,.0f}", border=True)

with col2:
    st.write("3D Map")
    pydeck_chart(df_land_bronx, "bronx")

st.write("")

# staten island
col1, col2 = st.columns(2) 

with col1:
    st.write("Staten Island")

    with st.container():
        st.metric("The number of sold properties", f"{num_staten:,.0f}", border=True)

    with st.container():
        st.metric("The average price of sold properties", f"${avg_staten:,.0f}", border=True)
    
    with st.container():
        st.metric("The maximum price of sold properties", f"${max_staten:,.0f}", border=True)

with col2:
    st.write("3D Map")
    pydeck_chart(df_land_staten, "staten")

st.write("")