import folium
from folium.plugins import HeatMap
import pandas as pd
import numpy as np
from branca.colormap import linear
from branca.colormap import LinearColormap
import json
import os

def fatalities_circle(data, district_coords,
                      markers,
                       map_height = 2000, 
                       map_width = 2000,
                       heatmap_colors = ['yellow', 'purple'],
                        heatmap_range = [0, 2500],):
    
    m = folium.Map(location=[31.5, 35.30], 
                   zoom_start=8, 
                   width=map_width, 
                   height=map_height)
    # Create a base map centered around the region
    folium.TileLayer('openstreetmap' ).add_to(m)
    

    colormap = LinearColormap(
        colors=heatmap_colors,
        vmin= heatmap_range[0],
        vmax=heatmap_range[1]  
    )

    colormap.caption = 'Deaths per district'
    colormap.add_to(m)
    
    # data_file_path = os.path.abspath(data)
    # print(data_file_path)
    # print(data)
    with open(data, 'r') as file:
        data = file.read()
    
    data = json.loads(data)

    yearly_district_fatalities = pd.Series(data)
    for year, year_data in yearly_district_fatalities.groupby(level=0):
        layer = folium.FeatureGroup(name=str(year), overlay=False, control=True)
        for district, coord in district_coords.items():
            fatalities = data[year][district]
            if markers:
                folium.Marker(
                    location=coord,
                    tooltip=f'{district}: {fatalities} fatalities',
                    icon=None
                ).add_to(layer)
            folium.Circle(
                    location=district_coords[district],
                    radius=np.sqrt(data[year][district]) * 1000, 
                    color=colormap(data[year][district]),
                    fill=True,
                    fill_color=colormap(data[year][district]),
                    fill_opacity=0.6,
                ).add_to(layer)
        layer.add_to(m)
    


    folium.LayerControl(collapsed=False, control=False).add_to(m)

    return m