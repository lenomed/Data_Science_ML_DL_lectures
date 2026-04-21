import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('ticks')

sns.set_context('poster')
plt.figure(figsize=(12,20))
tips = sns.load_dataset("tips")
sns.lmplot(x='total_bill', y='tip', data= tips, palette='seismic', hue='sex')
sns.despine()
plt.show()