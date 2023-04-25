import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, rainfall_amounts = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            current_date_rainfall_amount = float(row[3])
        except ValueError:
            print(f"There are missing data at {current_date}")
        else:
            dates.append(current_date)
            rainfall_amounts.append(current_date_rainfall_amount)

# Plot graphic
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall_amounts, alpha=0.5)
plt.fill_between(dates, rainfall_amounts, facecolor='yellow', alpha=0.2)

# Plot format
plt.title('Rainfall amount - Death Valley, CA 2018', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Daily rainfall (m)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
