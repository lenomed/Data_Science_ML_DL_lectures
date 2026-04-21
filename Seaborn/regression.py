import matplotlib.pyplot as plt
import seaborn as sns

# lm plot allows you to display linear models with seaborn

tips = sns.load_dataset('tips')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], scatter_kws={'s': 20})
plt.show()