#ignoring OS usage warnings from tensor flow
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#importing Tensor flow
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential  # ✅
from keras.layers import Dense

#split data
from sklearn.model_selection import train_test_split

#importing scaler
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\NN_Neural_Networks\fake_reg.csv')
print(df.head(10))

X = df.drop(columns=['price']).to_numpy()
y=df['price'].to_numpy()

X_train, X_test, y_train,y_test=train_test_split(X,y, test_size=.4, random_state=101)


#instnciate scaler

scaler =MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# creating a neural network

model = Sequential()

model.add(Dense(4,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(1))

model.compile(optimizer='rmsprop', loss='mse')
model.fit(x=X_train,y=y_train, epochs=250)

loss_df= pd.DataFrame(model.history.history)

loss_df.plot()
plt.show()
