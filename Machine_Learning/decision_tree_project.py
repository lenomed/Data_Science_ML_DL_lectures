import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

#Index(['credit.policy', 'purpose', 'int.rate', 'installment', 'log.annual.inc',
       #'dti', 'fico', 'days.with.cr.line', 'revol.bal', 'revol.util',
      # 'inq.last.6mths', 'delinq.2yrs', 'pub.rec', 'not.fully.paid'],
      #dtype='object')

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\loan_data.csv')
print(df.head())
print(df.info())
print(df.describe())


#debt_consolidation
#credit_card
#cleaning data
df['purpose'] = df['purpose'].map({'debt_consolidation': 1, 'credit_card':0 })
print(df.head())

# data visualization and studies

plt.figure(figsize=(10,6))
df[df['credit.policy']==1]['fico'].hist(alpha=0.5,color='blue',
                                              bins=30,label='Credit.Policy=1')
df[df['credit.policy']==0]['fico'].hist(alpha=0.5,color='red',
                                              bins=30,label='Credit.Policy=0')
plt.legend()
plt.show()


plt.figure(figsize=(10,6))
df[df['not.fully.paid']==1]['fico'].hist(alpha=0.5,color='blue',
                                              bins=30,label='not.fully.paid=1')
df[df['not.fully.paid']==0]['fico'].hist(alpha=0.5,color='red',
                                              bins=30,label='not.fully.paid=0')
plt.legend()
plt.xlabel('FICO')
plt.show()

plt.xlabel('FICO')

plt.figure(figsize=(11,7))
sns.lmplot(y='int.rate',x='fico',data=df,hue='credit.policy',
           col='not.fully.paid',palette='Set1')
plt.show()

plt.figure(figsize=(11,7))
sns.countplot(x='purpose',hue='not.fully.paid',data=df,palette='Set1')
plt.show()

sns.jointplot(x='fico',y='int.rate',data=df,color='purple')
plt.show()

#assing values fot x and y
X=df.drop('not.fully.paid', axis=1)
y= df['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.4, random_state=101)

dtree = DecisionTreeClassifier()

dtree.fit(X_train, y_train)

d_pred = dtree.predict(X_test)

print(classification_report(y_test, d_pred))


# we use a single decision tree for prediction here


# let's use multiple decision tress for prediction

r_forest = RandomForestClassifier(n_estimators=200)
r_forest.fit(X_train, y_train)

r_pred = r_forest.predict(X_test)

print(classification_report(y_test, r_pred))