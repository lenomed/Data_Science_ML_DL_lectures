import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import GridSearchCV

#instaciate the dataset
cancer = load_breast_cancer()
print(cancer.keys())

df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
df['target'] = cancer['target']
print(df.head(10))

X=df.drop('target', axis=1)
y=df['target']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.4, random_state=101)

#instanciate the model
model = SVC()

model.fit(X_train, y_train)

pred = model.predict(X_test)

# checking performance of model
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
# finding best parameters for C and gamma of 
# C controls the cost of misclassification a learge C value gives you low variance and high bias
param_grid={'C':[0.1,10,100,1000],'gamma':[1,0.1,0.01,0.001,0.0001]}
grid=GridSearchCV(SVC(), param_grid, verbose=3)

print(grid.fit(X_train,y_train))
print(grid.best_params_)

grid_pred = grid.predict(X_test)

print(confusion_matrix(y_test, grid_pred))
print('/n')
print(classification_report(y_test, grid_pred))