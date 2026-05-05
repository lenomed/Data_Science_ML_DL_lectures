import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\Classified Data', index_col=0)
print(df.head())
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
print(scaled_features)

#creating a df for the scaled data

df_features = pd.DataFrame(scaled_features, columns=df.columns[:-1])
print(df_features)

X = df_features
y = df['TARGET CLASS']

#split data :train test split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.4, random_state=101)

knn = KNeighborsClassifier(n_neighbors=24)
 
#training the model
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)

print(classification_report(y_test, predictions))

#Using the elbow method to choose the best k value
error_rate =[]

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error rate')
plt.show()