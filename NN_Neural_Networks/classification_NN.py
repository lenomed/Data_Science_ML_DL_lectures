import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential  # ✅
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\NN_Neural_Networks\cancer_classification.csv')
print(df.head(10))
print(df.info())

X=df.drop('benign_0__mal_1', axis=1).values
y=df['benign_0__mal_1'].values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2, random_state=101)

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# initial model, it only had the sequential neurons and some basic parameters
# no Dropout, callbacks, earlystops, which made it to overfit
model = Sequential()

model.add(Dense(30, activation='relu'))
model.add(Dense(15, activation='relu'))

# the last neuron is gonna be sigmoid because it is a binary classification
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')

model.fit(x=X_train, y=y_train, epochs=600, validation_data=(X_test,y_test))

mod_histo = pd.DataFrame(model.history.history)
print(mod_histo.head(10))

mod_histo.plot()
plt.show()

# this is the second model, it has earlystopps, and callbacks but it do not have dropouts
# this second model over fitted, the val_loss was shooting up like crazy
early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=25,restore_best_weights=True)
model.fit(x=X_train, y=y_train, epochs=600, validation_data=(X_test,y_test), callbacks=[early_stop])

mod_histo2 = pd.DataFrame(model.history.history)
print(mod_histo2.head(10))

mod_histo2.plot()
plt.show()

# this the third model on this particular code base or file
# i added dropout, earlystopps, callacks to increase the performance of this last model
model2 = Sequential()

model2.add(Dense(30, activation='relu'))
model2.add(Dropout(rate=.5))

model2.add(Dense(15, activation='relu'))
model2.add(Dropout(rate=.5))

model2.add(Dense(1, activation='sigmoid'))

model2.compile(loss='binary_crossentropy', optimizer='adam')

early_stops = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=25,restore_best_weights=True)
model2.fit(x=X_train, y=y_train, epochs=600, validation_data=(X_test,y_test), callbacks=[early_stops])

mod_histo3 = pd.DataFrame(model2.history.history)
print(mod_histo3.head(10))

mod_histo3.plot()
plt.show()

predictions = (model2.predict(X_test) > 0.5).astype(int)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))