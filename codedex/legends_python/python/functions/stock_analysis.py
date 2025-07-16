"""
Instructions
In fintech, we often perform a time series analysis on stocks. This means that we need to analyze a stock, given its price over a certain time. 📈

In this exercise, we will perform a simplified version of a time series analysis. The stock that we will be analyzing is the $AMC stock in January 2023.

Here are the stock prices (in dollars) for each of these weekdays:

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

Create a stock_analysis.py program that implements three functions:

price_at(x) that finds the price on a given day x.
max_price(a, b) that finds the maximum price from day a to day b.
min_price(a, b) that finds the minimum price from day a to day b.
The parameters of the days will be in the range of 1 to 20 (since that is the period for the stock we are analyzing).

Make sure to call each function to test if your functions work correctly!

"""


stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]


def prices_at(x):
  return stock_prices[x-1]

def max_price(a,b):
  # return max(stock_prices[a - 1: b])
  mx = 0
  for i in range(a, b + 1):
    mx = max(mx, prices_at(i))
  return mx

def min_price(a, b):
  min_num = prices_at(a)
  for i in range(a, b + 1):
    min_num = min(min_num, prices_at(i))
  return min_num



print(max_price(1, 15))
print(min_price(5, 10))
print(prices_at(3))
