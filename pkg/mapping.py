import pydeck as pdk
import streamlit as st
from pkg.property_functions import to_residential_type

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

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
    df = df.dropna(subset=["sale_price", "latitude", "longitude", "building_class_category"])
    df = df[(df["sale_price"] > 0) & (df["land_square_feet"] > 0)]
    df['price_per_sf'] = df['sale_price'] / df['land_square_feet']
    df['price_per_sf_display'] = df['price_per_sf'].apply(lambda x: f"${x:,.0f}")

    # classify building class
    df['building_class_category'] = df['building_class_category'].apply(to_residential_type)

    # color
    building_type_colors = {
        'Other': '#FF0000',       # red
        '3 Family': '#00FF00',    # green
        '2 Family': '#FFA500',    # orange
        '1 Family': '#0000FF',    # blue
    }
    df['color'] = df['building_class_category'].map(lambda x: hex_to_rgb(building_type_colors.get(x, '#808080')))

    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(
                latitude=latitude,
                longitude=longitude,
                zoom=10,
                pitch=45,
            ),
            layers=[
                pdk.Layer(
                    "ColumnLayer",
                    data=df,
                    get_position='[longitude, latitude]',
                    get_elevation="price_per_sf",
                    elevation_scale=0.5,
                    radius=50,
                    get_fill_color="color",
                    pickable=True,
                    auto_highlight=True,
                )
            ],
            tooltip={"text": "Building Type: {building_class_category}\nPrice/SF: {price_per_sf_display}"}
        )
    )

# @st.cache_resource
# def pydeck_chart(df, boro):

#     center_coords = {
#         "manhattan": (40.7831, -73.9712),
#         "brooklyn": (40.6782, -73.9442),
#         "queens": (40.7282, -73.7949),
#         "bronx": (40.8448, -73.8648),
#         "staten": (40.5795, -74.1502)
#     }

#     latitude, longitude = center_coords.get(boro)

#     # filtering
#     df = df.dropna(subset=["sale_price", "latitude", "longitude"])
#     df = df[(df["sale_price"] > 0) & (df["land_square_feet"] > 0)]
#     df['price_per_sf'] = df['sale_price'] / df['land_square_feet']

#     # mapping
#     st.pydeck_chart(
#         pdk.Deck(
#             map_style=None,
#             initial_view_state=pdk.ViewState(
#                 latitude=latitude,
#                 longitude=longitude,
#                 zoom=10,
#                 pitch=50,
#             ),
#             layers=[
#                 pdk.Layer(
#                     "HexagonLayer",
#                     data=df,
#                     get_position="[longitude, latitude]",
#                     get_elevation="price_per_sf",
#                     radius=100,
#                     elevation_scale=4,
#                     elevation_range=[0, 1000],
#                     pickable=True,
#                     extruded=True,
#                 )
#             ],
#         )
#     )