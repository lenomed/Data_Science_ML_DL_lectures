import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

from sklearn.model_selection import train_test_split

#'Email', 'Address', 'Avatar', 'Avg. Session Length', 'Time on App',
  #     'Time on Website', 'Length of Membership', 'Yearly Amount Spent'

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\Ecommerce Customers')
print(df.columns)
print(df.info())
print(df.describe())
print(df.head())

# they are note closely related
sns.jointplot(x=df['Time on Website'], y=df['Yearly Amount Spent'])
plt.show()

sns.jointplot(x=df['Time on App'], y=df['Yearly Amount Spent'])
plt.show()

sns.jointplot(x=df['Time on App'], y=df['Length of Membership'], kind='hex')
plt.show()

sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()

sns.lmplot(x='Yearly Amount Spent', y='Length of Membership', data=df)
plt.show()




# Training the data set

X=df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y=df['Length of Membership']

X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=0.4)

#creating an instance of a LM

lm = LinearRegression()
lm.fit(X_train, y_train)

#print out coeficients

cdf = pd.DataFrame(lm.coef_, X.columns,columns=[['coef']])

#predicting Test Data

predictions = lm.predict(X_test)
print(cdf.head())

#scatter plot of test Value

plt.scatter(y_test, predictions)
plt.title='Linear regression prediction'
plt.show()

mse = metrics.mean_squared_error(y_test, predictions)
mae = metrics.mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mse)

print(f'mean squared error{mse}, mean absolute error{mae}, root mean squared error{rmse}')

# residuals are the difference between the actual value and the predicted value

residuals = y_test - predictions

plt.hist(residuals)
plt.show()

cdf2 = pd.DataFrame(lm.coef_, X.columns,columns=[['coef']])
print(cdf2.head())
