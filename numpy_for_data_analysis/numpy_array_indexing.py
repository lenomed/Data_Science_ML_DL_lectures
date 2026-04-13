import numpy as np

#array indexing in numpy................
arr= np.arange(11)
print(arr[3])# you can use slice notation here

print(arr[:5]) # this returns values from the start of the array to the index that you marked as the stop
# the space at the back of the colon represents zero while you can still replace with 5 and replace rthe position of 5 wisth nothing and get values from 5 to the end of the array

#the difference between python arrays and numpy array is the ability of np to broad cast
arr[0:5]=100
print(arr)

slice_of_arr = arr[:5]
slice_of_arr[:5]=100
print(slice_of_arr)

arr_copy = arr.copy()
arr_copy[:]=100
print(arr_copy)

#indexing 2d array in numpy

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
index_of_array = arr_2d[0][2] # while using single bracket you'll arr_2d[3,3] the value of the rows and columns are separated by comma
print(arr_2d)
print(index_of_array)
#indexing more than one part of the matrix

multi_mat =arr_2d[1:, 0:]
print(multi_mat)

arr = np.arange(0,11)
mask = arr > 5
print(arr[arr >5])# conditional selection
print(mask)

create_mat = np.arange(50).reshape(5,10)
make_mat = create_mat[3:5,8:10]
print(create_mat)
print(make_mat)

