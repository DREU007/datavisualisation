import csv
from datetime import datetime

import matplotlib.pyplot as plt


class ExtractedData:
    """Initialize attributes filename location, and low and high row number"""
    def __init__(self, filename):
        self.filename = filename

        # Prepare data from csv for a matplotlib.pyplot
        with open(self.filename) as f:
            reader = csv.reader(f)
            row_header = next(reader)

            for index, column_header in enumerate(row_header):
                print(index, column_header)
                if column_header == 'TMIN':
                    self.tlowrow = index
                elif column_header == 'TMAX':
                    self.tmaxrow = index
                elif column_header == 'TAVG':
                    self.tavgrow = index

            self.dates, self.lows, self.highs, self.tavgs = [], [], [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                try:
                    low = int(row[int(self.tlowrow)])
                    high = int(row[int(self.tmaxrow)])
                    avg = int(row[int(self.tavgrow)])
                except ValueError:
                    print('The data is missing for {current_date}')
                else:
                    self.dates.append(current_date)
                    self.lows.append(low)
                    self.highs.append(high)
                    self.tavgs.append(avg)


filename1 = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'

d1 = ExtractedData(filename1)
d2 = ExtractedData(filename2)

# Sitka
fig, ax = plt.subplots()
ax.plot(d1.dates, d1.highs, c='red', alpha=0.5)
ax.plot(d1.dates, d1.lows, c='blue', alpha=0.5)
plt.fill_between(d1.dates, d1.highs, d1.lows, facecolor='red', alpha=0.1)

# Format
plt.title('Sitka - Death Valley Comparison\n2018', fontsize=24)
plt.ylabel('Temperature (F)', fontsize=20)
plt.xlabel('Yellow - Death Valley\nRed - Sitka', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
ax.axis([None, None, 20, 130])

# Death Valley
ax.plot(d2.dates, d2.highs, c=(1, 0.1, 0.1), alpha=0.5)
ax.plot(d2.dates, d2.lows, c=(0, 0, 0.5), alpha=0.6)
plt.fill_between(d2.dates, d2.highs, d2.lows, facecolor='yellow', alpha=0.3)

# T avg
fig, ax = plt.subplots()
ax.plot(d1.dates, d1.tavgs)
# ax.plot(d2.dates, d2.tavgs)

plt.show()
