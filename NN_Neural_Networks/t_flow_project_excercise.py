# removing compatibility warning and information
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
#//

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#standardize the data
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

#Image.Var	Image.Skew	Image.Curt	Entropy	Class
# spliting data

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# tensor
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
 

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\NN_Neural_Networks\bank_note_data.csv')

sns.countplot(x='Class', data=df)
plt.show()

sns.pairplot(df, hue='Class')
plt.show()

# Standardizing
scaler = StandardScaler()
scaler.fit(df.drop('Class', axis=1))

scaled_features = scaler.fit_transform(df.drop('Class', axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
print(df_feat.head())

# split data
X = df_feat.values
y= df['Class'].values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.4, random_state=101)

model = Sequential()

model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dropout(0.3))
model.add(Dense(20, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
es = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

mod_hist = model.fit(X_train, y_train, epochs=50, validation_data=(X_test,y_test), callbacks=[es])
print(mod_hist)

plt.plot(mod_hist.history['loss'])
plt.plot(mod_hist.history['val_loss'])
plt.plot(mod_hist.history['accuracy'])
plt.plot(mod_hist.history['val_accuracy'])
plt.legend(['loss', 'val_loss', 'accuracy', 'val_accuracy'])
plt.show()

predictions = (model.predict(X_test) > 0.5).astype(int)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

