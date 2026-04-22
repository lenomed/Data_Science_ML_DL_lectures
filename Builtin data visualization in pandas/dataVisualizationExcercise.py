from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.style.use('ggplot')

df = pd.read_csv('df3')
df.plot.scatter(x='b', y='a', cmap='coolwarm',s=50, c='red', figsize=(12,5))
print(df.head())

df['a'].hist()

df[['a','b']].plot.box()
plt.show()

df['d'].plot.kde(lw=20, ls='--')
plt.show()

ax = df.iloc[0:30].plot.area(alpha=0.4)
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
