import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

df =pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\KNN_Project_Data')
print(df.head())

#sns.pairplot(df, hue='TARGET CLASS')
#plt.show()
stds = StandardScaler()
stds.fit(df.drop('TARGET CLASS', axis=1))

stds_features = stds.transform(df.drop('TARGET CLASS', axis=1))

df_features = pd.DataFrame(stds_features, columns =df.columns[:-1])

print(stds_features)
print(df_features.head(10))

# after standardizing the data let's then implement our model and train it

#Define the x and the y values
X = stds_features
y= df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.4, random_state =101)

#instanciate the model

knn = KNeighborsClassifier(n_neighbors=27)
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)

print(classification_report(y_test, predictions))


# using the elbow method to choose a k value

error=[]

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    new_pred = knn.predict(X_test)
    error.append(np.mean(new_pred != y_test))

plt.plot(range(1,40), error, linestyle='dashed', color='blue', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error rate')
plt.show()