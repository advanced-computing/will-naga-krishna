import streamlit as st

st.set_page_config(page_title="Construction Information in NYC", page_icon="🏠")
st.sidebar.header("Construction Information in NYC")

st.title('Construction Information in NYC')
st.markdown("<h5 style='text-align: right;'>by Will & Naga & Krishna</h5>", 
            unsafe_allow_html=True)

st.header('Description',divider=True)
st.markdown('''
            This project takes maps of construction applications and prices of sold properties 
            in NYC and combines them to understand the relationship between the amount of 
            housing construction and the property prices.

            This project was developed in response to the rising cost of living throughout New York City and, in particular, the rising rents.
            This tool is meant to help understand how the city is responding to the lack of housing supply.
            ''')

st.header('Proposal',divider=True)
st.markdown('''
            **Research Questions**
            - What areas of the city (borough, community district, etc.) are seeing the most construction of housing? How many units can be expected?
            - What kinds of housing are being prioritized by the city? New developments? Renovations? Low density? High density? Luxury? Affordable?
            - Do people apply for construction permits in areas with high property prices?

            **Data Source**
            - [Construction Applications](https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Job-Application-Filings/w9ak-ipjd/about_data): Updated daily by the Department of Buildings. The table in Google Cloud is updated daily by the workflow we have set.
            - [Prices of Sold Properties](https://data.cityofnewyork.us/City-Government/NYC-Citywide-Annualized-Calendar-Sales-Update/w2pb-icbu/about_data): Updated annually by the Department of Finance. The most recent data available is only from 2022 at the moment.
            ''')

st.header('Benefits',divider=True)
st.markdown('''
            **For Private Sector**
            - ...
            - ...

            **For Public Sector**
            - ...
            - ...
            ''')