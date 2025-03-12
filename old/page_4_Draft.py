# import libraries
import streamlit as st
import pandas as pd
from sodapy import Socrata
import pydeck as pdk

# title
st.title("NYC Land Price Mapping - Will & Naga")
st.write("This is our first attempt at building a map of the land price data in Streamlit")

# read data from api
client = Socrata("data.cityofnewyork.us", None)
df_list = []
offset = 0

while len(df_list) < 10000:
        results = client.get("w2pb-icbu", limit=2000, offset=offset)
        offset += 2000
        df_list.extend(results)

# form dataframe
df_land = pd.DataFrame.from_records(df_list)
df_land[['sale_price', 'latitude', 'longitude']]

# create a function to transform data into float
def to_float(value: pd.Series):
    return value.astype(float)

# transform data into float
df_land['sale_price'] = to_float(df_land['sale_price'])
df_land['latitude'] = to_float(df_land['latitude'])
df_land['longitude'] = to_float(df_land['longitude'])

# delete the rows including 'Nan'
df_land.dropna(subset=["latitude", "longitude", "sale_price"], inplace=True)

# pydeck layer for visualization
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=40.71,
            longitude=-73.98,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df_land,
                get_position="[longitude, latitude]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df_land,
                get_position="[longitude, lattitude]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

# data source (https://data.cityofnewyork.us/City-Government/NYC-Citywide-Annualized-Calendar-Sales-Update/w2pb-icbu/about_data)