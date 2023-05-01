import json
from datetime import datetime as dt
from plotly.graph_objs import Layout
from plotly import offline


def get_time(timestamp):
    current_time = dt.fromtimestamp(timestamp / 1000)
    return current_time.strftime("%d-%m-%Y %H:%M:%S")


filename = 'data/1.0_month_april23.geojson'
with open(filename, encoding='UTF8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
title = f"{all_eq_data['metadata']['title']} <br>Total: {len(all_eq_dicts)}"

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
hover_texts = [
    f"{eq_dict['properties']['title']} <br>Time:"
    f" {get_time(eq_dict['properties']['time'])}" for eq_dict in all_eq_dicts
]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [2.5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='ex1_global_earthquakes.html')
