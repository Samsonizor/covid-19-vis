import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mode_to_file = {
    'Deaths': 'Deaths',
    'Recoveries': 'Recovered',
    'Cases': 'Confirmed'
}

location_major = 'China'
location_minor = 'Hubei'
# location_minor = None

# mode = 'Recoveries'
# mode = 'Deaths'
mode = 'Cases'

# plot_scale = 'log'
plot_scale = 'linear'

timeseries_csv_path = '../csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{}.csv'.format(mode_to_file[mode])

test = pd.read_csv(timeseries_csv_path, nrows=443, parse_dates=True, index_col=[1,0], keep_default_na=False)
test = test.T
test = test.drop(['Lat', 'Long'], axis=0)
print(test)
if location_minor:
    title = 'COVID-19 {} in {}, {}'.format(mode, location_minor, location_major)
    test[location_major][location_minor].plot()
else:
    title = 'COVID-19 {} in {}'.format(mode, location_major)
    test[location_major].plot()

plt.yscale(plot_scale)
plt.grid(True, which="both")
plt.title(title)
plt.show()
