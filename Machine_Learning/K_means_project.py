import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#'Unnamed: 0', 'Private', 'Apps', 'Accept', 'Enroll', 'Top10perc',
     #  'Top25perc', 'F.Undergrad', 'P.Undergrad', 'Outstate', 'Room.Board',
      # 'Books', 'Personal', 'PhD', 'Terminal', 'S.F.Ratio', 'perc.alumni',
#'Expend', 'Grad.Rate'

df =pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\College_Data')
 

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

#data visualization and analysis
df['Private'] = df['Private'].map({'Yes': 1, 'No': 0})
plt.scatter(x='Grad.Rate', y='Room.Board', c= 'Private', cmap='rainbow',data=df)
#plt.show()

plt.scatter(x='F.Undergrad',y='Outstate', c='Private', cmap='viridis', data=df)
#plt.show()

g = sns.FacetGrid(df, hue="Private", palette='coolwarm', height=6, aspect=2)
g = g.map(plt.hist, 'Outstate', bins=20, alpha=0.7)
#plt.show()

sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',height=6,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)
#plt.show()

print(df[df['Grad.Rate']>100])
df.loc['Cazenovia College', 'Grad.Rate'] = 100

df.dropna(inplace=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df['Private'].astype=int
kmeans = KMeans(n_clusters=2)
kmeans.fit(df)

#creating cluster labels

kmeans = KMeans(n_clusters=2)

kmeans.fit(df)
print(kmeans.cluster_centers_)

df['Cluster']= pd.DataFrame(df['Private'])
print(f' this is the pro: {df['Private']}')
print(df.head())