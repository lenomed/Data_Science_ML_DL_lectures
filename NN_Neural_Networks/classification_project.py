import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\NN_Neural_Networks\loan_data.csv')
print(df.head(10))

df = df.drop('purpose', axis=1)
print(df.info())

plt.figure(figsize=(12,4))
sns.heatmap(df.corr())
plt.show()