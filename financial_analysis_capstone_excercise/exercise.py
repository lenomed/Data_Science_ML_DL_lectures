import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


sns.set_style('whitegrid')


start = datetime.datetime(2006, 1, 1)
end   = datetime.datetime(2016, 1, 1)

# Download all at once
df = yf.download(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'], start=start, end=end)

# Fix column order (new yfinance swaps levels)
df.columns = df.columns.swaplevel(0, 1)
df.sort_index(axis=1, inplace=True)

# Split into individual banks
BAC = df["BAC"]
C   = df["C"]
GS  = df["GS"]
JPM = df["JPM"]
MS  = df["MS"]
WFC = df["WFC"]

print(BAC.head())

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis=1, keys=tickers)

bank_stocks.columns.names = ['Bank Ticker','Stock Info']
print(f"max close price for each bank's stock:{bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()}")
print(f'these are bank stock {bank_stocks.head()}')

returns = pd.DataFrame()

for tick in tickers:
     returns[tick + ' return'] = bank_stocks[tick]['Close'].pct_change()

print(returns.head())

sns.pairplot(returns[1:])

plt.show()

worst = returns.idxmin()
print(worst)

best = returns.idxmax()
print(best)

st_div = returns.loc['2015-01-01':'2015-12-31'].std()
print(st_div)

df2 = pd.DataFrame()
df3 = pd.DataFrame()

for tick in tickers:
    df2['MS'] = bank_stocks['MS']['Close'].pct_change()

print(f'this is for morgan stanley: {df2.loc['2015']}')

sns.histplot(df2.loc['2015'])
plt.show()

for tick in tickers:
    df3['C'] = bank_stocks['C']['Close'].pct_change()

sns.histplot(df3.loc['2015'])
plt.title='citi group'
plt.show()


returns2 = pd.DataFrame()

stock_infos = bank_stocks.xs(key='Close', axis=1, level='Stock Info');
print(f'this is the stock info print out: {stock_infos.head()}')
stock_infos.plot()
plt.show()

# two ways to do one thing

#for tick in tickers:
 #    returns2[tick + ' return'] = bank_stocks[tick]['Close'].plot()
#print(returns.head())
#plt.tight_layout()
#plt.show()


