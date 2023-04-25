import csv
from datetime import datetime

from plotly.graph_objs import Layout, Scattergeo
from plotly import offline


filename = 'data/J1_VIIRS_C2_Global_7d.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_title in enumerate(header_row):
        print(index, column_title)

    lons, lats, dates_times, temperatures = [], [], [], []
    for row in reader:
        time = (str(row[5]) + ' ' + str(row[6]))
        lons.append(row[1])
        lats.append(row[0])
        dates_times.append(datetime.strptime(time, '%Y-%m-%d %H%M'))
        temperatures.append(float(row[2]))

    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': dates_times,
        'marker': {
            'size': [temperature * 1 for temperature in temperatures],
            'color': temperatures,
            'colorscale': 'Hot',
            'reversescale': True,
            'colorbar': {'title': 'Kelvin Temperature'}
        }
    }]

my_layout = Layout(title='Fires for 7 days')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig)
