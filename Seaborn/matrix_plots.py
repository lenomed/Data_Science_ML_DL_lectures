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
sns.heatmap(flights_matrix, cmap='coolwarm')
plt.tight_layout()
plt.show()
print(flights_matrix)