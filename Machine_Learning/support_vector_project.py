import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

df = sns.load_dataset('iris')
sns.countplot(x='species', data=df)
plt.show()
print(df.head(20))
print(df.keys())

#don't use getdummies on SVC model because it can handle multiple classes automatically, you don't need to convert species to dummies. get_dummies is needed for features (X), not for the target (y).
#SVC encodes y automatically for you instead of trying the getdummies
#flower_species = pd.get_dummies(df['species'], dtype=int)
#df = pd.concat([df, flower_species], axis=1)
#df.drop('species', axis=1, inplace=True)
#print(df.head(20))

# defining x and y for the model
X = df.drop('species', axis=1)
y=df['species']

#splitting the data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.4, random_state=101)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#instantiating the model
model = SVC()
model.fit(X_train, y_train)

#predicting/ testing the model
model_pred = model.predict(X_test)

#looking up model performance
print(confusion_matrix(y_test, model_pred))
print(classification_report(y_test, model_pred))

param_grid = {'C':[0.1,10,100,1000], 'gamma':[1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']}

g_search = GridSearchCV(SVC(), param_grid, verbose=3)

g_search.fit(X_train, y_train)

grid_pred = g_search.predict(X_test)

print(g_search.best_params_)  

print(g_search.best_params_)
print(g_search.best_score_)

print(classification_report(y_test, grid_pred))
print('\n')
print(confusion_matrix(y_test, grid_pred))