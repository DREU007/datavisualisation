import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/1.0_month.geojson'
with open(filename, encoding='UTF-8') as f:
    all_data = json.load(f)

title_name = all_data['metadata']['title']
eq_dicts = all_data['features']
mags = [eq_dict['properties']['mag'] for eq_dict in eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in eq_dicts]
hover_texts = [eq_dict['properties']['title'] for eq_dict in eq_dicts]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [mag*2.5 for mag in mags],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale':  True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title=title_name)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig)