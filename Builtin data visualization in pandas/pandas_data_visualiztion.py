import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv('df1', index_col=0)
df1['A'].plot(kind='hist')
plt.show()

df2 = pd.read_csv('df2')
df2.plot(kind='hist')
df2.plot.area(alpha=0.5)
df2.plot.bar()
plt.show()


df = pd.DataFrame(np.random.randn(1000,2), columns=['a', 'b'])
df.plot.hexbin(x='a', y='b', gridsize=25)
plt.show()

df['a'].plot.kde()
plt.show()
