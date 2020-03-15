import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mode_to_file = {
    'Deaths': 'Deaths',
    'Recoveries': 'Recovered',
    'Cases': 'Confirmed'
}

location_major = 'Spain'
# location_minor = 'Sichuan'
location_minor = None

plot_scale = 'log'
# plot_scale = 'linear'

plot_style = 'area'
# plot_style = 'line'

csv_path_formattable = '../csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{}.csv'

timeseries_csv_path_deaths     = csv_path_formattable.format(mode_to_file['Deaths'])
timeseries_csv_path_recoveries = csv_path_formattable.format(mode_to_file['Recoveries'])
timeseries_csv_path_cases      = csv_path_formattable.format(mode_to_file['Cases'])

data_deaths = pd.read_csv(timeseries_csv_path_deaths, nrows=443, parse_dates=True, index_col=[1,0], keep_default_na=False).T.astype(int)
data_recoveries = pd.read_csv(timeseries_csv_path_recoveries, nrows=443, parse_dates=True, index_col=[1,0], keep_default_na=False).T.astype(int)
data_cases = pd.read_csv(timeseries_csv_path_cases, nrows=443, parse_dates=True, index_col=[1,0], keep_default_na=False).T.astype(int)

data_deaths = data_deaths.drop(['Lat', 'Long'], axis=0)
data_recoveries = data_recoveries.drop(['Lat', 'Long'], axis=0)
data_cases = data_cases.drop(['Lat', 'Long'], axis=0)

data_active_cases = data_cases-data_recoveries-data_deaths

data_deaths.columns = pd.MultiIndex.from_tuples([(a, b, 'deaths') for a,b in data_deaths.columns], names=('major location','minor location','status'))
data_recoveries.columns = pd.MultiIndex.from_tuples([(a, b, 'recoveries') for a,b in data_recoveries.columns], names=('major location','minor location','status'))
data_active_cases.columns = pd.MultiIndex.from_tuples([(a, b, 'active cases') for a,b in data_active_cases.columns], names=('major location','minor location','status'))

data = pd.merge(data_recoveries, data_deaths, left_index=True, right_index=True)
data = pd.merge(data, data_active_cases, left_index=True, right_index=True)

if location_minor:
    title = 'COVID-19 in {}, {}'.format(location_minor, location_major)
    data_subset = data[location_major][location_minor]
else:
    title = 'COVID-19 in {}'.format(location_major)
    data_subset = data[location_major]

if plot_style == 'line':
    data_subset.plot()
else:
    data_subset.plot.area()

plt.yscale(plot_scale)
plt.grid(True, which="both")
plt.title(title)
plt.xlabel('date')
plt.ylabel('people')
plt.ylim(bottom=1)
plt.show()
