#multi index nd index heirachy
from numpy.random import randn
import numpy as np
import pandas as pd

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
print(list(zip(outside,inside)))
hier_index = list(zip(outside,inside))# the zip method combines two lists item by item
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,["A", "B"])
df.index.names = ["Groups", "Num"]
get_mat_val = f"this is my mat output: {df.loc["G1"].loc[2]["B"]}"
print(get_mat_val)
print(df)

#xs method or the cross section methods

cross_section = df.xs(1, level="Num")# it is kinda easier to navitgate with it than the loc() method
print(cross_section)