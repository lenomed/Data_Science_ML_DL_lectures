import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
g = sns.PairGrid(iris)
g.map_diag(sns.histplot)
g.map_upper(sns.kdeplot)
g.map_lower(plt.scatter)
g.map(plt.scatter)
plt.show()

tips = sns.load_dataset('tips')
f_grid = sns.FacetGrid(data=tips, col='time', row='smoker')
f_grid.map(sns.histplot, 'total_bill')
plt.show()

