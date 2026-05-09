import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# spliting our data

from sklearn.model_selection import train_test_split

#the model

from sklearn.naive_bayes import MultinomialNB
# evaluating model
from sklearn.metrics import classification_report, confusion_matrix

#pipeline
from sklearn.pipeline import Pipeline


yelp_df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\yelp.csv')
print(yelp_df.head(10))
print(yelp_df.describe())
print(yelp_df.info())

yelp_df['text length'] = yelp_df['text'].apply(lambda x: len(x.split()))
print(yelp_df.head(10))

#yelp_df['text length'].astype(str)

g = sns.FacetGrid(yelp_df, col='stars')
g.map(plt.hist, 'text length')
plt.show()

sns.boxplot(x='stars', y='text length', data=yelp_df)
plt.show()

sns.countplot(x='stars', data=yelp_df)
plt.show()

mean_df = yelp_df.select_dtypes(include=['number'])
print(mean_df)

mean_df_group = mean_df.groupby('stars').mean()
print(mean_df_group)
print('$'*50)
print('\n')
correlated = mean_df_group.corr()
print(correlated)

sns.heatmap(correlated)
plt.show()

yelp_class = yelp_df[(yelp_df.stars==1) | (yelp_df.stars==5)]
print(yelp_class.tail(7))

X = yelp_class['text']
y = yelp_class['stars']

# instanciating Vectorizer

yelp_vector = CountVectorizer()
X=yelp_vector.fit_transform(X)

X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=.4, random_state=101)

# instanciating and training the model

nb = MultinomialNB()
nb.fit(X_train, y_train)

predictions = nb.predict(X_test)

print(classification_report(y_test, predictions))
print('*'*50)
print(confusion_matrix(y_test, predictions))

#Using Text processing or pipeline
X = yelp_class['text']
y = yelp_class['stars']
X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=.4, random_state=101)

pipeline = Pipeline([
        ('bow', CountVectorizer()),#string to token integer counts
        ('tfidf', TfidfTransformer()),# integer counts to weighted TF-IDF scores
        ('classifier', MultinomialNB())# train on TF-IDF vectors w/ Naive Bayes Classifier
    ])

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

