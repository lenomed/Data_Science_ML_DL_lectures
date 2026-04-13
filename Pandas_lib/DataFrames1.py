# Data frame is a bunch of series that shares thesame index
import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5,4),["A","B","C","D","E"], ["W","X","Y","Z"])
print(df)
index_frame = df.W #df["W"] you can still use this to get the column in W
multi_frames = df[["X","Y","Z"]] # used to print multi frames
print(multi_frames)
print(index_frame)

# to add new column
new_col = df["new"] = df["W"] + df["X"]
print(df)
df.drop("new", axis=1, inplace=True)
print(df)

#ROWS

row_axis = df.loc["A"]
print(row_axis)

row_axis2 = df.iloc[2]
print(row_axis2)

#you can actually use indexing just like numpy to get a chunk of data from a matrix using the loc() method

get_mat = df.loc[["A","B"], ["W","Y"]]
print(get_mat)