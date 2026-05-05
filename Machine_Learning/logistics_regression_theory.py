import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#models
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


train = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\titanic_train.csv')
print(train.head())


#sns.heatmap(train.isnull())
#plt.show()
#sns.countplot(x='Survived', data=train, hue='Sex')
#plt.show()
s
# dealing with missing data 'Age'

def inpute_Age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

train['Age'] = train[['Age', 'Pclass']].apply(inpute_Age, axis=1)

# in the cabin column there is a lot of missing data therefor it will be droped entrirely

train.drop('Cabin', axis =1, inplace=True)
train.dropna(inplace=True)

#sns.heatmap(train.isnull())
#plt.show()

#converting categorical data into dummy variable using pandas

sex = pd.get_dummies(train['Sex'], drop_first=True,dtype=int)
embark = pd.get_dummies(train['Embarked'], drop_first=True,dtype=int)
passenger_class = pd.get_dummies(train['Pclass'], drop_first=True, dtype=int)

train = pd.concat([train, sex, embark, passenger_class], axis=1)

train.drop('Pclass', inplace=True, axis=1)
train.drop(['Sex','Embarked','Name', 'Ticket'], axis=1, inplace=True)
train.drop(['PassengerId'], axis=1 ,inplace=True)

print(train.head(10))

cols = ['Age', 'Parch', 'Fare', 'male']  # 'male' is your dummy column for gender

#sns.heatmap(train[cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
#plt.title('Correlation Matrix')
#plt.show()
#plt.show()

print(train['Fare'])
print(train.head())

#using map and functions 

#train['Sex'] = train['Sex'].map({'male': 1, 'female': 0}) this particula line of code is faster and does thesame thing with the function below


# def inpute_sex(row):
   # if row['Sex'] == 'male':
      # return 1
    #elif row['Sex'] == 'female':
       # return 0
   # else:
       # return row['Sex']

#train['Sex'] = train.apply(inpute_sex, axis=1)

#train['Embarked'] = train['Embarked'].map({'S':1, 'C':0})

#print(train['Sex'])

# CLEANING THE TEST DATA

test = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\titanic_test.csv')


#cleaning data-------------
test['Age'] = test[['Age', 'Pclass']].apply(inpute_Age, axis=1)

def impute_fare(cols):
    Fare = cols[0]
    Pclass = cols[1]

    if pd.isnull(Fare):
        if Pclass == 1:
            return 60
        elif Pclass == 2:
            return 15
        else:
            return 8
    else:
        return Fare

test['Fare'] = test[['Fare', 'Pclass']].apply(impute_fare, axis=1)


test_sex = pd.get_dummies(test['Sex'], drop_first=True, dtype=int)
test_embark = pd.get_dummies(test['Embarked'], drop_first=True, dtype=int)
test_passenger_class = pd.get_dummies(test['Pclass'], drop_first=True, dtype=int)

test = pd.concat([test, test_sex, test_embark, test_passenger_class], axis=1)

test.drop('Cabin', inplace=True, axis=1)
#test.dropna(inplace=True)
test.drop('Pclass', inplace=True, axis=1)
test.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
test.drop(['PassengerId'], axis=1, inplace=True)

test.columns = test.columns.astype(str)
print(test.head(10))
#sns.heatmap(test.isnull())
#plt.show()
#print(test.head())
#print(test.tail())
#print('*'*50)
#print(f'this is the length of fare{len(test['Fare'])-len(test['Q'])}')

############################################### test data cleaned

# Creating the model

X= train.drop('Survived', axis=1)
y=train['Survived']

#print(f'survived: {y}')
#print(f' not survived: {X['Q']}')

X.columns = X.columns.astype(str)
X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=.3, random_state=101)

#calling the model
lm = LogisticRegression()

#training the model
lm.fit(X_train,y_train)

predictions = lm.predict(X_test)


print(classification_report(y_test, predictions))

 
# Testing with a new test data


def label_output():
    new_data = lm.predict(test)
    return ['Survived' if x == 1 else 'Died' for x in new_data]

print(label_output())
