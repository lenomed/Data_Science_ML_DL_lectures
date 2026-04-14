# Conditional Selection
import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5,4),["A","B","C","D","E"], ["W","X","Y","Z"])
booldf = df > 0
print(booldf)
change_bool = df[booldf]
print(change_bool)

booldf2 = df[df > 0]
print(booldf2)

get_col = df["W"]>0
print(get_col)
resultdf = df[df["W"]>0]["X"]# you can [["X". "Y"]]  which would return 2 columns
print(resultdf)
#C row was removed because it has -2 which i less than zero at the begining of the row
multi_cond = df[(df["W"]>0) & (df["Y"]>1)]
print(multi_cond) # it will print the row that meets the condition
df.reset_index(inplace=True)# inplace = True keeps changes permanent
new_in = "CA BA YU IU HU".split()
df["states"]=new_in
print(df)
# how to set index

df.set_index("states", inplace=True)
print(df)