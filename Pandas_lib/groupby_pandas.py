import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
df_sum = df.groupby('Company').sum()
print(df_sum)
print("---------------------------------------")
df_loc = df.groupby('Company')
loca = df_loc.sum().loc['FB']
print(loca)
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
print(df)