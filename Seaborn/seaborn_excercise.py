from multiprocessing import Value
import matplotlib.pyplot as plt
from numpy._core import numeric
import seaborn as sns
import pandas as pd

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.head())
sns.jointplot(x='age', y='fare', data=titanic)

plt.show();

# Load Titanic dataset directly from seaborn's hosted CSV
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Plot fare distribution
#df['Fare'].plot(kind='hist', color='salmon', edgecolor='white')
#plt.xlabel('fare')
#plt.show()

sns.distplot(titanic['fare'], color='salmon', kde=False, bins=30)
plt.show()

'''titanic['class_label'] = titanic['pclass'].map({
    1: 'First',
    2: 'Second',
    3: 'Third'
})
'''
sns.boxplot(x='class', y='age', data= titanic)
plt.show()
# Boxplot
#sns.boxplot(x='class_label', y='age', data=titanic)
#plt.show() 

# Swarmplot (separate figure)
#sns.swarmplot(x='class_label', y='age', data=titanic)
#plt.show()

sns.swarmplot(x='class', y='age', data=titanic, palette='coolwarm')
plt.show()

sns.countplot(x='sex', data=titanic)
plt.show()

sns.heatmap(titanic.corr(numeric_only=True))
plt.show()

m = sns.FacetGrid(col='sex', data=titanic)
m.map(plt.hist, 'age')
plt.show()