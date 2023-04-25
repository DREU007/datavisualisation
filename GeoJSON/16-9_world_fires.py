import csv
from datetime import datetime

from plotly.graph_objs import Layout, Scattergeo
from plotly import offline
from math import sqrt
import plotly as plt


#num_rows = 25_000
filename = 'data/J1_VIIRS_C2_Global_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_title in enumerate(header_row):
        print(index, column_title)

    row_num = 0
    lons, lats, dates_times, temperatures = [], [], [], []
    for row in reader:
        if row[8] == 'high':
            time = (str(row[5]) + ' ' + str(row[6]))
            lons.append(row[1])
            lats.append(row[0])
            dates_times.append(datetime.strptime(time, '%Y-%m-%d %H%M'))
            temperatures.append(float(row[10]))
            row_num += 1
    #print(len(dates_times))
        #if row_num == num_rows:
            #break

y = datetime.toordinal(dates_times[-1]) - datetime.toordinal(dates_times[0])
opacity_time = []
for date_time in dates_times:
    x = datetime.toordinal(dates_times[-1])-datetime.toordinal(date_time)
    opacity_time.append(1-x/y)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': dates_times,
    'marker': {
        'size': [temperature/60 for temperature in temperatures],
        'color': temperatures,
        'colorscale': 'YlOrRd',
        'colorbar': {'title': 'Brightness - Kelvin'},
        'opacity': opacity_time,
        'symbol': '300',
    }
}]

my_layout = Layout(title='Global Fire Activity')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
