import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn import metrics


df= pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\USA_Housing.csv')

print(df.head())

print(df.columns)

X=df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
y  =df['Price']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.4, random_state=101)

lm=LinearRegression()
lm.fit(X_train, y_train)

cdf = pd.DataFrame(lm.coef_,X.columns, columns=[['Coef']])
print(cdf.head())

predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Actual Price (Correct Value)')
plt.ylabel('Predicted Price')
plt.show()

#calculating Error metric

mae = metrics.mean_absolute_error(y_test, predictions)
print(f' mean absolute error: {mae}')
mse = metrics.mean_squared_error(y_test, predictions)
print(f'means squared error: {mse} ')
rmse = metrics.root_mean_squared_error(y_test, predictions)
print(f'root mean squared error: {rmse}')   