import csv

from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, precipitations, totals = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            precipitation = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            precipitations.append(precipitation)
            if totals:
                totals.append(totals[-1] + precipitation)
            else:
                totals.append(precipitation)
                

    fig = plt.figure(dpi=128, figsize=(10,5))
    plt.plot(dates, precipitations, c='blue', alpha=0.6)
    plt.fill_between(dates, precipitations, facecolor='blue', alpha=0.3)

    plt.plot(dates, totals, c='blue', alpha=0.1)
    plt.fill_between(dates, totals, facecolor='blue', alpha=0.09)

    #format plot
    title = "Daily precipitation amounts and cumulative precipitation - 2014\nSitka, AK"
    plt.title(title, fontsize=18)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel('Precipitation', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()
