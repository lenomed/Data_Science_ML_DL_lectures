import numpy as np
import pandas as pd

lables = ["a", "b", "c"]
my_list = [1,2,3]
arr = np.array(my_list)#numpy array
d = {"a": 10, "b": 20, "c": 30}

serie= pd.Series(data = my_list)
#serie_label = pd.Series(data = my_list, index = lables) // this code also works
serie_label = pd.Series(my_list, lables)
serie_label2 = pd.Series(arr, lables)# passing np array inside the series method
print(serie_label2)
print(serie)
print(serie_label)
print(pd.Series(d))
# Series can hold in built in methods as data points

#printing data from Series
ser1 = pd.Series([1,2,3,4],["usa", "ussr","japan", "china"])
ser2 = pd.Series([1,2,3,4],["usa", "ussr","korea", "china"])
add_ser = ser1+ser2
print(add_ser)
print(ser1["usa"])

