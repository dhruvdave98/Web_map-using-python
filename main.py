# -----------------------------------------------------------
# demonstrates how to point out geolocation on the world map and
# point out the latitude and longitude of the volcanoes using python-folium
#
# email dhruvdave61@gmail.com
# ----------------------------------------------------------

import folium
import pandas

# Read the local txt file, which contains the data of volcanoes
# and extract the latitude, longitude and elevation from it
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


# This function sets color of the volcanoes' spot according to the elevation of it.
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# folium.Map() function defines the latitude and longitude of the initial location on the world map
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# adding volcanoes in the feature group and sets the default color of the volcanoes' spots
fgv = folium.FeatureGroup(name="Volcanoes")
for lat, lon, el in zip(lat, lon, elev):
    fgv.add_child(
        folium.CircleMarker(location=[lat, lon], popup=str(el) + " m", fill_color=color_producer(el), color='grey',
                            fill_opacity=0.7))

# adding population in the feature group and sets different color of all the countries according to its population
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
