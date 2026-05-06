import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8, random_state=101)
print(data)
plt.scatter(data[0][:,0],data[0][:,1], c=data[1], cmap='rainbow')
plt.show()

print(data[1]) 

kmeans=KMeans(n_clusters=4)
kmeans.fit(data[0])

print(kmeans.labels_)

fig,(axis1,axis2)=plt.subplots(1,2, sharey=True, figsize=(10,6))
axis1.set_title('K Means')
axis1.scatter(data[0][:,0],data[0][:,1], c=kmeans.labels_, cmap='rainbow')

axis2.set_title('Original')
axis2.scatter(data[0][:,0],data[0][:,1], c=data[1], cmap='rainbow')

plt.show()