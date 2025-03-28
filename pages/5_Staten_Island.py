# import libraries
import streamlit as st
from pkg.mapping import pydeck_chart
from pkg.to_float import to_float
from pkg.load_data_property import connect_to_data_staten

# title
st.title("Staten Island")

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
df_land = connect_to_data_staten(table)

# transform data into float
df_land['sale_price'] = to_float(df_land['sale_price'])
df_land['land_square_feet'] = to_float(df_land['land_square_feet'])
df_land['latitude'] = to_float(df_land['latitude'])
df_land['longitude'] = to_float(df_land['longitude'])

# number of sold properties
num = len(df_land)

# avg price of sold properties
avg = df_land['sale_price'].mean()

# avg price per land square foot
avg_price_per_sqft = df_land['sale_price'].mean() / df_land['land_square_feet'].mean()

# maximum price of sold properties
max = round(df_land['sale_price'].max(), 2)

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
        st.metric("The average price of sold properties per square feet", 
                  f"${avg_price_per_sqft:,.0f}", border=True)
    
    with st.container():
        st.metric("The maximum price of sold properties", f"${max:,.0f}", border=True)

with col2:
    pydeck_chart(df_land, "staten")

with col3:
    st.write('''
    - The height and color of the dots in the map are based on the relative prices of sold properties. 
    ''')