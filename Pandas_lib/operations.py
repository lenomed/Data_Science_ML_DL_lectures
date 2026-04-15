import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df_head = df.head()
print(df_head)
print("_"*50)
df_unique = df["col2"].unique()
print(df_unique)
print("_"*50)
df_nunuique = df["col2"].nunique()
print(df_nunuique)
print("_"*50)
df_lambda = df["col2"].apply(lambda x:x*2)
print(df_lambda)
print("_"*50)
df_value_count = df['col2'].value_counts()
print(df_value_count)
print("_"*50)
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(newdf)
print("_"*50)
print(df.columns)
print("_"*50)
print(df.index)
print("_"*50)
print(df.sort_values(by=['col2']))
print("_"*50)
df2 = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()
print(df2.fillna("Fill"))

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
data_f = pd.DataFrame(data)


print("_"*50)
df_pivot = data_f.pivot_table(values="D", index=['A', 'B'], columns=['C'])
print(df_pivot)