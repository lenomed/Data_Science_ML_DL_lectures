from operator import index
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.head())
flights = sns.load_dataset('flights')
tip_corr = tips.select_dtypes(include='number').corr()

sns.heatmap(tip_corr, annot=True, cmap='coolwarm')
plt.show()

heat_flight = flights.select_dtypes(include='number').corr()
plt.show()

flights_matrix = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(flights_matrix, cmap='coolwarm', linecolor='#ffff', linewidths='1')# maga in cmap can be used to display data from warm to cool, just like anti clock wise but not realy, it gives you the opposite of the supposed display method
plt.tight_layout()
plt.show()
print(flights_matrix)

#it uses heirachical clustering to display the clustered values of the data

sns.clustermap(flights_matrix, standard_scale=1)
plt.show()