import pandas as pd
import quandl as qd
import matplotlib.pyplot as plt
import numpy as np

qd.ApiConfig.api_key = '<your API Key>'

aapl_data = qd.get('EOD/MSFT', start_date="2010-01-01", end_date="2020-01-01")
Apple = aapl_data.head()
# print(Apple)

# Calculate the Returns
close_price = aapl_data[['Adj_Close']]
daily_return = close_price.pct_change()
daily_return.fillna(0, inplace=True)
# print(daily_return)

adj_price = aapl_data[['Adj_Close']]

# Calculate the moving average
mav = adj_price.rolling(window=50).mean()

# Print the results
print(mav[-10:])

adj_price.plot()
mav.plot()
plt.show()
