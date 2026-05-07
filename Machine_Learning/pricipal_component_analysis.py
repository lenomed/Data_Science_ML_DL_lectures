import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# PCA is used for component reduction
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#instantiate the data
cancer = load_breast_cancer()

df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])

scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

# PCA algorithm
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)
print(scaled_data.shape)
print(x_pca.shape)

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('First principal component')
plt.ylabel('Second Principal Component')
plt.show()
