import csv
from datetime import datetime

from plotly.graph_objs import Layout
from plotly import offline


def get_time(current_date, current_time):
    target = f"{current_date} {current_time}"
    return datetime.strptime(target, "%Y-%m-%d %H%M")


filename = 'data/J1_VIIRS_C2_Global_7d_30april23.csv'
with open(filename) as f:
    data = f.readlines()

reader = csv.reader(data)
header_ind = {head: ind for ind, head in enumerate(next(reader))}

i_lat = header_ind["latitude"]
i_lon = header_ind["longitude"]

i_date = header_ind["acq_date"]
i_time = header_ind["acq_time"]

i_confidence = header_ind["confidence"]
i_temp = header_ind["bright_ti5"]


lons, lats, dates, temperatures = [], [], [], []
for row in reader:
    if row[i_confidence] == 'high':
        date = (get_time(row[i_date], row[i_time]))
        lons.append(row[i_lon])
        lats.append(row[i_lat])
        dates.append(get_time(row[i_date], row[i_time]))
        temperatures.append(float(row[i_temp]))

max_time = max(dates)
min_time = min(dates)
time_delta = max_time - min_time
opacity_time = []
for date_time in dates:
    current_date_delta = date_time - min_time
    opacity_time.append(current_date_delta / time_delta)


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': dates,
    'marker': {
        'size': [temperature / 60 for temperature in temperatures],
        'color': temperatures,
        'colorscale': 'YlOrRd',
        'colorbar': {'title': 'Brightness - Kelvin'},
        'opacity': opacity_time,
        'symbol': '300',
    }
}]

title = (
    f'Global Fire Activity'
    f' {min_time.strftime("%d.%m.%Y")}-{max_time.strftime("%d.%m.%Y")}'
)

my_layout = Layout(title=title)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='ex3_world_fires.html')
