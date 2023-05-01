import csv
from datetime import datetime

import matplotlib.pyplot
import matplotlib.pyplot as plt


class ExtractedData:
    """Initialize attributes filename location, and low and high row number"""
    def __init__(self, filename):
        self.filename = filename

        # Prepare data from csv for a matplotlib.pyplot
        with open(self.filename) as f:
            file = f.readlines()

        reader = csv.reader(file)

        header_ind = {head: ind for ind, head in enumerate(next(reader))}

        i_date = header_ind["DATE"]
        i_tmin = header_ind["TMIN"]
        i_tmax = header_ind["TMAX"]

        self.dates, self.lows, self.highs = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[i_date], '%Y-%m-%d')
            try:
                low = int(row[i_tmin])
                high = int(row[i_tmax])
            except ValueError:
                print(f'The data is missing for {current_date}')
            else:
                self.dates.append(current_date.date())
                self.lows.append(low)
                self.highs.append(high)


filename1 = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'

d1 = ExtractedData(filename1)
d2 = ExtractedData(filename2)

fig, ax = plt.subplots()

# Sitka
ax.plot(d1.dates, d1.highs, c='red', alpha=0.5)
ax.plot(d1.dates, d1.lows, c='blue', alpha=0.5)
plt.fill_between(d1.dates, d1.highs, d1.lows, facecolor='black', alpha=0.2)

# Death Valley
ax.plot(d2.dates, d2.highs, c=(1, 0.1, 0.1), alpha=0.5)
ax.plot(d2.dates, d2.lows, c=(0, 0, 0.5), alpha=0.6)
plt.fill_between(d2.dates, d2.highs, d2.lows, facecolor='yellow', alpha=0.3)

plt.title('Sitka - Death Valley Comparison\n2018', fontsize=24)
plt.ylabel('Temperature (F)', fontsize=20)
plt.xlabel('Yellow - Death Valley\nGray - Sitka', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

ax.axis([datetime(2018, 1, 1), datetime(2019, 1, 1), 20, 130])

plt.show()
