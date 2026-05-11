from ipywidgets.widgets.widget_controller import Axis
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df =pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\NN_Neural_Networks\kc_house_data.csv')
print(df.head())
print(df.columns)


sns.heatmap(df.isnull())# you can isnull().sm() id you don't want to use heatmap to check for missing values
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(df['price'])
plt.show()

df.drop('date', axis=1, inplace=True)
#using plotly to visualize the hist of df:price
#fig = px.histogram(df['price'])
#fig.show()

#df.drop('')
# you can use .corr().sort_values to check the correlation of data instead of using a heat map
print(df.corr()['price'].sort_values())

plt.scatter(x='price', y='sqft_living', data=df)
plt.show()

plt.figure(figsize=(12,6))
sns.scatterplot(x='long', y='lat', data=df)
plt.show()

# removing or trimming outliers

trim_outliers = df.sort_values(by='price', ascending=False).iloc[216:]

print(trim_outliers.sort_values(by='price', ascending=False))

plt.figure(figsize=(12,6))

sns.scatterplot(x='long', y='lat', data=trim_outliers)

plt.show()