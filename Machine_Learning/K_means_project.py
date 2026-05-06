import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\College_Data')

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# convert Private to numeric
df['Private'] = df['Private'].map({'Yes': 1, 'No': 0})

# data visualization
plt.scatter(x='Grad.Rate', y='Room.Board', c='Private', cmap='rainbow', data=df)
plt.show()

plt.scatter(x='F.Undergrad', y='Outstate', c='Private', cmap='viridis', data=df)
plt.show()

g = sns.FacetGrid(df, hue="Private", palette='coolwarm', height=6, aspect=2)
g = g.map(plt.hist, 'Outstate', bins=20, alpha=0.7)
plt.show()

sns.set_style('darkgrid')
g = sns.FacetGrid(df, hue="Private", palette='coolwarm', height=6, aspect=2)
g = g.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.7)
plt.show()

# fix Grad.Rate > 100
print(df[df['Grad.Rate'] > 100])
df.loc[df.index[df['Unnamed: 0'] == 'Cazenovia College'][0], 'Grad.Rate'] = 100

# clean data
df.dropna(inplace=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)

# save Private labels before dropping
private_labels = df['Private'].copy()

# fit KMeans on features only (without Private)
kmeans = KMeans(n_clusters=4, random_state=101)
kmeans.fit(df.drop('Private', axis=1))

print(kmeans.cluster_centers_)

# assign cluster labels
df['Cluster'] = kmeans.labels_

# evaluate against Private labels
print(confusion_matrix(private_labels, df['Cluster']))
print(classification_report(private_labels, df['Cluster']))