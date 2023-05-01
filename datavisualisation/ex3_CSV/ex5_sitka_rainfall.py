import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    file = f.readlines()

reader = csv.reader(file)
header_ind = {head: ind for ind, head in enumerate(next(reader))}
i_date = header_ind["DATE"]
i_rain = header_ind["PRCP"]

dates, rainfall_amounts = [], []
for row in reader:
    current_date = datetime.strptime(row[i_date], '%Y-%m-%d')
    try:
        current_date_rainfall_amount = float(row[i_rain])
    except ValueError:
        print(f"There are missing data at {current_date}")
    else:
        dates.append(current_date.date())
        rainfall_amounts.append(current_date_rainfall_amount)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, rainfall_amounts, alpha=0.5)
plt.fill_between(dates, rainfall_amounts, facecolor='blue', alpha=0.2)

plt.title('Rainfall amount - Sitka, AK 2018', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Daily rainfall (m)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
