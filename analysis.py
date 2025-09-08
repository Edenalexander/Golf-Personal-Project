from statsmodels.nonparametric.smoothers_lowess import lowess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#Loading the golf data frame

df = pd.read_csv("Golf_Scores.csv")
df['Over Par'] = df['Score'] - df['Par']

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.sort_values('Date')

#How my score has changed over time

round_totals = df.groupby('Date')['Over Par'].sum().reset_index()


round_totals = round_totals.sort_values('Date')
round_totals['Game'] = range(1, len(round_totals) + 1)
print(round_totals['Game'].dtype)
print(round_totals)

#Creating scatter plot - displaying how my golf scores has changed over time

scatter = round_totals.plot(kind='scatter', x='Game', y='Over Par')
plt.title("How my 'Over Par' changed over 21 Games")
x = np.arange(len(round_totals))
y = round_totals['Over Par']
m, b = np.polyfit(x, y, 1)
smoothed = lowess(round_totals['Over Par'], round_totals['Game'], frac=0.3)
plt.plot(round_totals['Game'], m*x + b, label='Best Fit')
plt.xticks(rotation=45)
plt.show()


# Hypothesis testing to see if i can draw conclusions from my line of best fit

x = round_totals['Game']
y = round_totals['Over Par']
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print(f"Slope: {slope}")
print(f"p-value: {p_value}")
plt.show()

#What hole do I find the hardest and why?

hole_totals = df.groupby('Hole')['Over Par'].sum().reset_index()
hole_totals['Avg Over Par'] = hole_totals['Over Par'] / len(round_totals)
hole_totals.plot(kind= 'bar', x= 'Hole', y= 'Avg Over Par')
plt.show()

#Which hole have I improved the most on?

#Splitting my games up into first 10 and last 11 to see how my scores have changed over time

df['Game'] = range(1, len(df) + 1)
first_10_games = df[df['Game'] <= 180]
last_11_games = df[df['Game'] >= 181]

#Creating first 10 df and last 11 df

first_10_games_with_holes = first_10_games.groupby('Hole')['Over Par'].sum().reset_index()

last_11_games_with_holes = last_11_games.groupby('Hole')['Over Par'].sum().reset_index()

first_10_games_with_holes['Avg Over Par'] = first_10_games_with_holes['Over Par'] / first_10_games.groupby('Hole')['Over Par'].count().values
last_11_games_with_holes['Avg Over Par'] = last_11_games_with_holes['Over Par'] / last_11_games.groupby('Hole')['Over Par'].count().values
print(first_10_games_with_holes)
print(last_11_games_with_holes)

#bar chart for first 10 games

first_10_games_with_holes.plot(kind= 'bar', x= 'Hole', y= 'Avg Over Par', color = 'red')
plt.title("First 10 Games")
plt.show()

#bar chart for last 11 games

last_11_games_with_holes.plot(kind= 'bar', x= 'Hole', y= 'Avg Over Par', color = 'green')
plt.title("last 11 Games")
plt.show()

#Merging the first 10 and last 11 df

combined_df = pd.merge(first_10_games_with_holes, last_11_games_with_holes, on='Hole', suffixes=('_First10', '_Last11'))
combined_df

#Quantifying how much my first 10 games compares with my last 11 games

combined_df['Hole Improvements'] = combined_df['Avg Over Par_First10'] - combined_df['Avg Over Par_Last11']
combined_df

#bar chart showing "Hole Improvements"

combined_df.plot(kind = 'bar', x = 'Hole', y = 'Hole Improvements')
plt.show()

#How my score compares with the Temperature

over_par_vs_temp
over_par_vs_temp = df.groupby('Date').agg({'Over Par': 'sum', 'Temperature (C)' : 'first'}).reset_index()
over_par_vs_temp.plot(kind='scatter', x='Over Par', y = 'Temperature (C)', title='Temperature vs Performance')
x = over_par_vs_temp['Over Par']
y = over_par_vs_temp['Temperature (C)']
m, b = np.polyfit(x, y, 1)
smoothed = lowess(y, x, frac=0.3)
plt.plot(x, m*x + b, label='Best Fit')
plt.show()

#Hypothesis test to see if I can conclude that temperature effects my golf scores

x = over_par_vs_temp['Over Par']
y = over_par_vs_temp['Temperature (C)']
slope, intercept, r_value, p_value, std_err = linregress(x,y)
print(f"Slope: {slope}")
print(f"p value: {p_value}")
plt.show()

over_par_vs_wind = df.groupby('Date').agg({'Over Par': 'sum', 'Wind (mph)' : 'first'}).reset_index()
over_par_vs_wind.plot(kind = 'scatter', x='Over Par', y = 'Wind (mph)', title = 'Wind Speed vs Performance')
x = over_par_vs_wind['Over Par']
y = over_par_vs_wind['Wind (mph)']
m, b = np.polyfit(x, y, 1)
smoothed = lowess(y, x, frac=0.3)
plt.plot(x, m*x + b, label='Best Fit')
plt.show()

#Hypothesis test to see if I can conclude that wind speeds effects my golf scores

slope, intercept, r_value, p_value, std_err = linregress(x,y)
print(f"Slope: {slope}")
print(f"p_value: {p_value}")
