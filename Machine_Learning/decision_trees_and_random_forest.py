import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#dex(['Kyphosis', 'Age', 'Number', 'Start'], dtype='object')
df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\kyphosis.csv')
#print(df.columns)

X= df.drop('Kyphosis', axis=1)
y=df['Kyphosis']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.4, random_state=101)

d_tree = DecisionTreeClassifier()
d_tree.fit(X_train, y_train)

pred = d_tree.predict(X_test)

print(classification_report(y_test, pred))

########## Using random forest because decision trees are prone to over fitting and bias

rfs = RandomForestClassifier(n_estimators=200)
rfs.fit(X_train, y_train)

pred = rfs.predict(X_test)

print(f'the below classification is random forest')
print(classification_report(y_test, pred))