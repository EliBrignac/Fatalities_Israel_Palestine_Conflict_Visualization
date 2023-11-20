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

from fatalities_circle import fatalities_circle
from fatalities_square import fatalities_square
from fatalities_heatmap import fatalities_heatmap

# Load the CSV into a dataframe
#data_df = pd.read_csv('fatalities_isr_pse_conflict_2000_to_2023.csv')
# Define the district coordinates



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


# Streamlit app
st.title("District Fatalities Heatmap")
st.write("This map shows the fatalities in different districts.")

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
 
st.markdown(
    """
    <style>
    div[class*="stRadio"] > label > div[data-testid="stRadio"] > label {
        font-size: 64px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

data_file = data_selection_to_file[data_formating]

if map_type == "Circles":
    m = fatalities_circle(data_file, district_coords, markers)
elif map_type == "Squares":
    m = fatalities_square(data_file, district_coords, markers)
elif map_type == "Heatmap":
    m = fatalities_heatmap(data_file, district_coords, markers)


m.control_scale = True
st_folium(m, 900, width=725)







