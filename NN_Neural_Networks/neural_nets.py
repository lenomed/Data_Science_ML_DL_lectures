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

#model evaluation

from sklearn.metrics import mean_absolute_error, mean_squared_error

#Saving trained models

from keras.models import load_model

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\NN_Neural_Networks\fake_reg.csv')
print(df.head(10))

X = df.drop(columns=['price']).to_numpy()
y=df['price'].to_numpy()

X_train, X_test, y_train,y_test=train_test_split(X,y, test_size=.4, random_state=101)


#instnciate scaler

scaler =MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Scaling Y, 
y_scaler = MinMaxScaler()
y_train = y_scaler.fit_transform(y_train.reshape(-1,1))
y_test = y_scaler.transform(y_test.reshape(-1,1))

# creating a neural network

model = Sequential()

model.add(Dense(4,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(1))

model.compile(optimizer='rmsprop', loss='mse')
model.fit(x=X_train,y=y_train, epochs=100)

loss_df= pd.DataFrame(model.history.history)

loss_df.plot()
plt.show()

#model evaluation with test data
print(model.evaluate(X_test,y_test, verbose=0))
print('\n *'*5)

print(model.evaluate(X_train,y_train, verbose=0))

test_predictions = model.predict(X_test)

test_predictions_inv = y_scaler.inverse_transform(test_predictions)
y_test_inv = y_scaler.inverse_transform(y_test)

pred_df = pd.DataFrame({
    'Test True Values': y_test_inv.flatten(),
    'Model Predictions': test_predictions_inv.flatten()
})

print(pred_df.head(10))

sns.scatterplot(data=pred_df, x='Test True Values', y='Model Predictions')
plt.plot([pred_df.min().min(), pred_df.max().max()],
         [pred_df.min().min(), pred_df.max().max()],
         'r--')
plt.show()

print(f'mean absolute error: {mean_absolute_error(pred_df['Test True Values'], pred_df['Model Predictions'])}')
print(f'mean squared error: {mean_squared_error(pred_df['Test True Values'], pred_df['Model Predictions'])}')

# testing model with a new data

new_gem = np.array([[998, 1000]])

new_gem_scaled = scaler.transform(new_gem)

pred_scaled = model.predict(new_gem_scaled)

pred = y_scaler.inverse_transform(pred_scaled)

print(f'new data pred: {pred}')

# loading model on another file
# model.save('my_model1.keras')
#later_model = load_model('my_model.keras')

#print(later_model.predict(new_gem))