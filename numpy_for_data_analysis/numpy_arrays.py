import numpy as np
from numpy.ma.core import argmax

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(np.array(my_list))

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(my_mat))

ranges = np.arange(0,25)
print(ranges)

## if you want to creat a list of zeros

zeross = np.zeros(4)
print(zeross)

print(np.zeros((3,3))) # you can do same for ones((5,5))

## lisnspace returns evenly spaced points in a range

print(np.linspace(0,6,10))

## identity matrix with numpy: it is the matrix of all zeros with 1 existing diagoaly in the matix

print(np.eye(3))

## random.rand, it generate number from a standard distribution of 0-1

print(np.random.rand(6)) # you can increase the dimenssion of the matrix by entering the stop or second argument in the rand function

## random.randn(): it generate numbers from 1 downwards

print(np.random.randn(3))

print(ranges.reshape(5,5))

## to locate the index of the max value of numbers in an array you use the argmax(array name)

print(argmax(ranges)) # you can do same with argmin(array name)

### you can check the shape of an array by using shape method
print(ranges.shape)

## dtype is used to know the data type that is in your array

print(ranges.dtype)
