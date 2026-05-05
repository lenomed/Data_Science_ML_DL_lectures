import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

ads = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\advertising.csv')

print(ads.head())
#sns.heatmap(ads.isnull())
#plt.show()

print(ads['Male'])

print(ads.info())
print(ads.describe())
print(ads['Age'].value_counts().head(10))
plt.hist(ads['Age'], bins=30)
plt.show()

sns.jointplot(x='Area Income',y='Age', data=ads)
plt.show()

sns.jointplot(x='Daily Time Spent on Site', y='Age', data=ads, kind='kde')
plt.show()

sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage', data=ads)
plt.show()

sns.pairplot(ads, hue='Clicked on Ad')
plt.show()


# The advertising dataset has text columns that will break the model
X = ads.drop(['Clicked on Ad', 'Ad Topic Line', 'City', 'Country', 'Timestamp'], axis=1)

y = ads['Clicked on Ad']
print(f'this is X: {X}')

X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=.4, random_state= 101)

log_model = LogisticRegression()
log_model.fit(X_train,y_train)

predictions = log_model.predict(X_test)

print(classification_report(y_test, predictions))
