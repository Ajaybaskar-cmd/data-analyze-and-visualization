import pandas.io as pd
import datetime
prices=pd.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2011,1,1),end=datetime.datetime(2013,1,1))['Adj Close']
print(prices.head())