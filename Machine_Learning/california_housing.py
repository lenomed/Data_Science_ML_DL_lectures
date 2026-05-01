import pandas as pd

import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

from sklearn import metrics

housing = fetch_california_housing()
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
housing_df['target'] = housing.target
print(housing_df.columns)

X = housing_df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup',
       'Latitude', 'Longitude']]

y = housing_df['target']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.4)

lm = LinearRegression()
lm.fit(X_train,y_train)

cdf = pd.DataFrame(lm.coef_,X.columns, columns=[['Coef']])
print(cdf.head())

predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.show()

