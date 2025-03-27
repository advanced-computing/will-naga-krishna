# import libraries
import streamlit as st
from pkg.mapping import pydeck_chart
from pkg.to_float import to_float
from pkg.load_data import connect_to_data_manhattan

# title
st.title("Manhattan")

# description
'''
This dashboard shows the following information in NYC:
- the permitted applications for new building construction from January 2024.
- the prices of properties sold in 2022.
'''

# construnction –> Will Part





# prorty price –> Naga Part

# load data
table='sipa-adv-c-naga-will.nyc_construction_property.property_price'
df_land = connect_to_data_manhattan(table)

# # classify the borough
# df_land['borough'] = df_land['borough'].apply(to_borough_name)
# df_land_manhattan = df_land[df_land['borough']=='Manhattan']

# transform data into float
df_land['sale_price'] = to_float(df_land['sale_price'])
df_land['latitude'] = to_float(df_land['latitude'])
df_land['longitude'] = to_float(df_land['longitude'])

# number of sold properties
num_manhattan = len(df_land)

# avg price of sold properties
avg_manhattan = df_land['sale_price'].mean()

# maximum price of sold properties
max_manhattan = round(df_land['sale_price'].max(), 2)

# delete the rows including 'Nan'
df_land.dropna(subset=["latitude", "longitude", "sale_price"], inplace=True)

# create a dashboard
st.write("")

# manhattan

col1, col2 = st.columns(2) 

with col1:
    with st.container():
        st.metric("The number of sold properties", f"{num_manhattan:,.0f}", border=True)

    with st.container():
        st.metric("The average price of sold properties", f"${avg_manhattan:,.0f}", border=True)
    
    with st.container():
        st.metric("The maximum price of sold properties", f"${max_manhattan:,.0f}", border=True)

with col2:
    pydeck_chart(df_land, "manhattan")