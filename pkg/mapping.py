import pydeck as pdk
import streamlit as st

@st.cache_resource
def pydeck_chart(df, boro):

    center_coords = {
        "manhattan": (40.7831, -73.9712),
        "brooklyn": (40.6782, -73.9442),
        "queens": (40.7282, -73.7949),
        "bronx": (40.8448, -73.8648),
        "staten": (40.5795, -74.1502)
    }

    latitude, longitude = center_coords.get(boro)

    # filtering
    df = df.dropna(subset=["sale_price", "latitude", "longitude"])
    df = df[df["sale_price"] > 0]

    # mapping
    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=latitude,
                longitude=longitude,
                zoom=10,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=df,
                    get_position="[longitude, latitude]",
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                )
            ],
        )
    )



    # st.pydeck_chart(
    #     pdk.Deck(
    #         map_style=None,
    #         initial_view_state=pdk.ViewState(
    #             latitude=latitude,
    #             longitude=longitude,
    #             zoom=10,
    #             pitch=50,
    #         ),
    #         layers=[
    #             pdk.Layer(
    #                 "HexagonLayer",
    #                 data=df,
    #                 get_position="[longitude, latitude]",
    #                 radius=200,
    #                 elevation_scale=4,
    #                 elevation_range=[0, 1000],
    #                 pickable=True,
    #                 extruded=True,
    #             ),
    #             pdk.Layer(
    #                 "ScatterplotLayer",
    #                 data=df,
    #                 get_position="[longitude, latitude]",
    #                 get_color="[200, 30, 0, 160]",
    #                 get_radius=200,
    #             ),
    #         ],
    #     )
    # )