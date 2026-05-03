import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\titanic_train.csv')
print(train.head())

print(train.isnull())

sns.heatmap(train.isnull())
plt.show()
sns.countplot(x='Survived', data=train, hue='Sex')
plt.show()

# dealing with missing data

