import numpy as np
import pandas as pd
d= {"A":[1,2,np.nan], "B":[1,np.nan, np.nan],"C": [1,2,3]}
df = pd.DataFrame(d)
print(df)
df_drop = df.dropna()# if you want to drop a column with a Null value the you specify the axis=?
print("........................................")
df_drop2 = df.dropna(axis=1)
print(df_drop2)
print("........................................")

threshna = df.dropna(thresh=2)# drops the row that has not more than one nan
print(df_drop)
print("........................................")
print(threshna)
fill_val = df["A"].fillna(value= df["A"].mean())
print(fill_val)