# Key Libraries
import numpy as np
import pandas as pd

# Global Datasets:
# Heights of basketball players for 'ballers()'
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
# Prices of houses for 'house_prices()'
market_prices = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
#DataFrame 

# Project #1: Basketball Players
def ballers():  
  mean = sum(players) / len(players)
  stdvar = (sum((v - mean) ** 2 for v in players) / len(players)) ** 0.5
  
  low, high = (mean - stdvar), (mean + stdvar)
  
  count = len([v for v in players if low < v < high])
  
  print(count)

ballers()

# Project #2: House Prices
def house_prices(data):
  mean = np.mean(data)
  deviation = np.std(data) 

  y1 = mean - deviation
  y2 = mean + deviation

  s = len(data [(data > y1) & (data < y2)])
  r = (s / len(data)) * 100
  
  print(r)

house_prices(market_prices)

# Project #3: COVID Data Analysis
def covid_data():
  df = pd.read_csv("/usercode/files/ca-covid.csv")

  df.drop('state', axis = 1, inplace = True)
  df.set_index('date', inplace = True)
  df['ratio'] = df['deaths'] / df['cases']

  print (df[df['ratio'] == df['ratio'].max()])

covid_data()