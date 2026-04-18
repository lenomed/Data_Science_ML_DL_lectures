import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style("whitegrid")

tips = sns.load_dataset("tips")
tips.head()
print(tips.head())

#It shows the average (by default) of a numeric
# value for each category.

sns.barplot(x="sex", y="tip", data=tips, estimator=np.std)
plt.show()

# count plot shows how many times each category appears
sns.countplot(x="sex", data=tips, label=['Gender', 'Tips'])
plt.show()

#Boxplot compares how a numeric variable is distributed across categories

sns.boxplot(x='day', y = 'total_bill', data=tips, color='red', hue='smoker')
plt.show()

#A violin plot shows the distribution of data, combining a boxplot + density plot.
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)# it gives the full shape of the data
plt.show()

# stripplot is a scatter plot based off of category
sns.stripplot(x='day', y='total_bill', data=tips, hue='sex',).legend(loc='best')
# jitter is used to decide how scatter plots are being displyed

plt.show()

#swwarmplot is similar to stripplot except the points are adjusted so they don't overlap
sns.swarmplot(x='day', y='total_bill', data=tips, dodge=True)
plt.show()# it is the combination of violinplot and strip plot

# the factor plot method is uses it's argument to call all the plot methods we have used above,
sns.catplot(x='day', y='total_bill', data=tips, kind='bar')
plt.show()