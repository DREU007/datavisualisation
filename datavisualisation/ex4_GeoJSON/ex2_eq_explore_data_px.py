import json
import datetime
import plotly.express as px


def get_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp / 1000)


filename = 'data/1.0_month_april23.geojson'
with open(filename, encoding='UTF8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
title = f"{all_eq_data['metadata']['title']} <br>Total: {len(all_eq_dicts)}"

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
names = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]
times = [get_time(eq_dict['properties']['time']) for eq_dict in all_eq_dicts]


max_time = max(times)
min_time = min(times)
time_delta = max_time - min_time

fig = px.scatter_geo(
    lat=lats, lon=lons, title=title,
    size=mags,
    color=mags,
    color_continuous_scale='Hot_r',
    labels={'color': 'Magnitude'},
    projection='natural earth',
    hover_name=[
        f"{name} <br>Time: {t.strftime('%d-%m-%Y %H:%M:%S')}"
        for name, t in zip(names, times)
    ],
    opacity=[(t - min_time).days / time_delta.days for t in times],
    )

fig.update_traces(marker_line_width=0)
fig.show()
