import folium
from folium.plugins import HeatMap
import pandas as pd
import numpy as np
from branca.colormap import linear
from branca.colormap import LinearColormap
import json


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
        vmax=heatmap_range[1]  # Adjust the range based on your data
    )

    colormap.caption = 'Deaths per district'
    colormap.add_to(m)
    
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
                    radius=np.sqrt(data[year][district]) * 1000,  # scale radius for better visualization
                    color=colormap(data[year][district]),
                    fill=True,
                    fill_color=colormap(data[year][district]),
                    fill_opacity=0.6,
                ).add_to(layer)
        layer.add_to(m)
    



    # Create a custom control with checkboxes for base layers
    base_layers = {
        'OpenStreetMap': folium.TileLayer('openstreetmap'),
    }

        # Add Layer Control to the map with type set to "checkbox" using a custom control
    folium.LayerControl(collapsed=False, control=False).add_to(m)

    # Save the map to an HTML file
    return m