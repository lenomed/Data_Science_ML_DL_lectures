import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df =pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\NN_Neural_Networks\kc_house_data.csv')
print(df.head())
print(df.columns)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


#importing Tensor flow
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential  # ✅
from keras.layers import Dense

#sns.heatmap(df.isnull())# you can isnull().sm() id you don't want to use heatmap to check for missing values
#plt.show()

#plt.figure(figsize=(10,6))
#sns.histplot(df['price'])
#plt.show()

df['date'] = pd.to_datetime(df['date'])
#using plotly to visualize the hist of df:price
#fig = px.histogram(df['price'])
#fig.show()

#df.drop('')
# you can use .corr().sort_values to check the correlation of data instead of using a heat map
print(df.corr()['price'].sort_values())

#plt.scatter(x='price', y='sqft_living', data=df)
#plt.show()

#plt.figure(figsize=(12,6))
#sns.scatterplot(x='long', y='lat', data=df)
#plt.show()

# removing or trimming outliers

trim_outliers = df.sort_values(by='price', ascending=False).iloc[216:]

print(trim_outliers.sort_values(by='price', ascending=False))

#plt.figure(figsize=(12,6))

#sns.scatterplot(x='long', y='lat', data=trim_outliers,edgecolor='none', alpha=0.2, palette='RdYlGn', hue='price')

#plt.show()

# the box plot shows that properties in water front is more costly than the ones on land
#sns.boxplot(x='waterfront', y='price', data=trim_outliers)
#plt.show()

#feature engineering 

df = df.drop('id', axis=1)

print(df.head())

df['year'] = df['date'].apply(lambda date: date.year) 
df['month'] = df['date'].apply(lambda date: date.month) 


df.groupby('year').mean()['price'].plot()
plt.show()

df = df.drop('date', axis=1)
df = df.drop('zipcode', axis=1)

# creating and training a model for prediction

#assigning and spliting data

X = df.drop('price', axis=1).to_numpy()

y= df['price'].to_numpy()

X_train, X_test, y_train,y_test=train_test_split(X,y, test_size=.4, random_state=101)

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# the number of the features determins the number of neurons created

model = Sequential()

model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')
# validation data helps check wether or not we are overfitting

model.fit(X_train,y_train, validation_data=(X_test,y_test), batch_size=128, epochs=400)
# the smaller the batchs size the slower the model training and the lesser it over fits

mod_hist = pd.DataFrame(model.history.history)

print(mod_hist.head(30))

mod_hist.plot()
plt.show()

single_house = df.drop('price', axis=1)iloc[0]

single_house = scaler.transform(single_house.reshape(-1,19))

print(model.predict(single_house))# the result here shows that we are shooting way higher than the range of the expected prediction

