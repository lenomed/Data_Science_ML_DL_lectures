import numpy as np

arr = np.arange(0,50)
add_array = arr+arr # you can actually do basic arithemetic operations
arr + 100 # this will add the scaler 100 to the whole numbers in the array, you can actually do basic arithemetic operations
print(add_array)

# you can perfomr operations like sqrt, exp, sine etc to the arrays of numpy
creat_mat = np.arange(0,1,0.01).reshape(10,10)
print(creat_mat)

create_mat2 = np.linspace(0,1,20)
print(create_mat2)