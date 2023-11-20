import streamlit as st
import folium
from branca.colormap import linear
import pandas as pd
import folium
import numpy as np
import plotly.express as px
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import time
from folium.plugins import HeatMap

# Map function imports
from folium_graphs.fatalities_circle import fatalities_circle
from folium_graphs.fatalities_square import fatalities_square
from folium_graphs.fatalities_heatmap import fatalities_heatmap



district_coords = {
    # CHECKED VIA GOOGLE
    # ( Degrees N , Degrees E)
    "Tulkarm" : (32.3191468, 35.0275505),
    "Jenin" : (32.4618837, 35.297566),
    "Jericho" : (31.8620094, 35.4610581),
    "Gaza" : (31.5, 34.4668),
    "Hebron" : (31.5326, 35.0998),
    "Tubas" : (32.3210552, 35.3689104),
    "Ramallah and al-Bira" : (31.9486212, 35.17004527911184),
    "East Jerusalem" : (31.7722541, 35.2156826),
    "Nablus" : (32.2222, 35.2623546),
    "Israel" : (31.0461, 34.8594762),
    "al-Quds" : (31.769767, 35.2137),
    "Bethlehem" : (31.7040336, 35.2096209),
    "Khan Yunis" : (31.3457612, 34.3025277),
    "Deir al-Balah" : (31.4183455, 34.3502476),
    "North Gaza" : (31.550126849999998, 34.519633),
    "Rafah" : (31.2968, 34.2435),
    "Qalqiliya" : (32.1960791, 34.9815019),
    "Salfit" : (32.0851611, 35.1815442),
    #"Gaza Strip" : (31.3547, 34.3088),
    "Gush Katif" : (31.21, 34.16),
}

data_selection_to_file = {
    "Yearly Fatalities" : "./data/yearly_fatalities.json",
    "Yearly Fatalities Rolling Sum" : "./data/yearly_fatalities_rolling_sum.json",
}


st.title("District Fatalities Heatmap")
st.write("""This map shows the fatalities in different districts of israel from the israel
          palestine conflict according to a kaggle dataset. The accuracy of the kaggle data 
         is outside of my control and may be subject to inaccuracies. This is just a fun project of mine.""")

# ======================= Sidebar =======================
st.sidebar.markdown("<h1 style='font-size: 48px;'>Options</h1>", unsafe_allow_html=True)

data_formating = st.sidebar.radio("Data Formating", ["Yearly Fatalities",
                                              "Yearly Fatalities Rolling Sum",
                                              ])

map_type = st.sidebar.radio("Map Type", ["Circles", "Squares",'Heatmap'])


markers = st.sidebar.checkbox("Show Markers", value=True)

st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 24px;
}
    </style>
    """, unsafe_allow_html=True)
col1, col2 = st.sidebar.columns(2)

# Add color pickers to each column
starting_color = col1.color_picker("Start Color", value="#FFFF00")
ending_color = col2.color_picker("End Color", value="#800080")


displayed_districts = district_coords.keys()
all_districts = st.sidebar.checkbox("All Districts", value=True)
if not all_districts:
    displayed_districts = st.sidebar.multiselect("Select Districts", list(district_coords.keys()), default=list(district_coords.keys()))

district_coords = {district: coord for district, coord in district_coords.items() if district in displayed_districts}
# ========================================================


# col1, col2 = st.columns(2)

# # ======================= Map =======================
# with col1:

data_file = data_selection_to_file[data_formating]
heatmap_colors=[starting_color, ending_color]
if map_type == "Circles":
    m = fatalities_circle(data_file, district_coords, markers, heatmap_colors=heatmap_colors)
elif map_type == "Squares":
    m = fatalities_square(data_file, district_coords, markers ,heatmap_colors=heatmap_colors)
elif map_type == "Heatmap":
    m = fatalities_heatmap(data_file, district_coords, markers, heatmap_colors=heatmap_colors)


m.control_scale = True
st_folium(m, 900, width=725)




# ========================================================


# ======================= General Graphs =======================
# with col2:
#     st.write("## General Graphs")
