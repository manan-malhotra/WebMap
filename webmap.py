import folium
import pandas

data = pandas.read_csv("volcano.csv")
lon = list(data["longitude"])
lat = list(data["latitude"])
elev = list(data["elevation"])
prim = list(data["primary"])


def color_producer(elevation):
    if elevation < 5000:
        return "yellow"
    if elevation < 6000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[19.251563, 74.142137], zoom_start=9)
fg = folium.FeatureGroup(name="Volcano Locations")
for lt, ln, el, pr in zip(lat, lon, elev, prim):
    if el < 4000 and el > 3000:
        fg.add_child(
            folium.CircleMarker(
                location=[lt, ln],
                popup=str(el) + "m",
                tooltip=str(pr),
                fill_color="darkblue",
                color="grey",
                radius=4,
                fill=True,
                fill_opacity=0.9,
            )
        )
    if el > 4205 and el < 6000:
        fg.add_child(
            folium.CircleMarker(
                location=[lt, ln],
                popup=str(el) + "m",
                tooltip=str(pr),
                fill_color=color_producer(el),
                color="grey",
                radius=6,
                fill=True,
                fill_opacity=0.6,
            )
        )
    if el > 6000:
        fg.add_child(
            folium.CircleMarker(
                location=[lt, ln],
                popup=str(el) + "m",
                tooltip=str(pr),
                fill_color=color_producer(el),
                color="grey",
                radius=9,
                fill=True,
                fill_opacity=0.8,
            )
        )

map.add_child(fg)
fm = folium.FeatureGroup(name="Home/College")
fm.add_child(
    folium.Marker(
        location=[19.251563, 73.142137],
        popup="Home Location",
        icon=folium.Icon("green"),
    )
)
fm.add_child(
    folium.Marker(
        location=[19.105946, 73.007312],
        popup="College Location",
        icon=folium.Icon("darkpurple"),
    )
)
map.add_child(fm)
map.add_child(folium.LayerControl())
map.save("Map1.html")
