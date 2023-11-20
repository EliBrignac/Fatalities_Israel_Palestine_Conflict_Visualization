import folium

# Create a base map
m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)

# Create some sample data for layers
data_layer1 = folium.FeatureGroup(name='Layer 1', overlay=False)
folium.Marker([37.7749, -122.4194], popup='Marker 1').add_to(data_layer1)
folium.Marker([37.7849, -122.4294], popup='Marker 2').add_to(data_layer1)

data_layer2 = folium.FeatureGroup(name='Layer 2', overlay=False)
folium.Marker([37.7649, -122.4094], popup='Marker 3').add_to(data_layer2)
folium.Marker([37.7949, -122.4394], popup='Marker 4').add_to(data_layer2)

# Add the layers to the map
data_layer1.add_to(m)
data_layer2.add_to(m)

# Add LayerControl to choose which layer shows up initially
folium.LayerControl(collapsed=False).add_to(m)

# Save the map to an HTML file
m.save('map_with_layers.html')

