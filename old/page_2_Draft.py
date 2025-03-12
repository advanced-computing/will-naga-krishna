import streamlit as st
import pandas as pd
from sodapy import Socrata
# import pydeck as pdk

st.markdown("# draft ❄️")
st.sidebar.markdown("# draft ❄️")

st.title("Will & Naga")
show_graph = st.radio("Do you want me to show the graph?", ("Yes", "No"), index=1)

if show_graph == "Yes":
    client = Socrata("data.cityofnewyork.us", None)
    df_list = []
    offset = 0

    while len(df_list) < 10000:
        results = client.get("ic3t-wcy2", limit=2000, offset=offset)
        offset += 2000
        df_list.extend(results)

    df = pd.DataFrame.from_records(df_list)

    # change the names of latitude and longitude
    df.rename(
        columns={
            "gis_latitude": "latitude",
            "gis_longitude": "longitude"
            },
        inplace=True)

    # delete the rows including 'Nan'
    df.dropna(subset=["latitude", "longitude", "job_type"], inplace=True)

    # transform to float
    df["latitude"] = df["latitude"].astype(float)
    df["longitude"] = df["longitude"].astype(float)

    # set colors for job_type
    color_map = {
        "A1": "#FF0000", # red
        "A2": "#00FF00", # green
        "NB": "#0000FF" # blue
    }
    df["color"] = df["job_type"].map(color_map).fillna("#808080")

    st.map(df, color="color")

else:
    st.write("See you soon!")