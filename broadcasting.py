import numpy as np

#array multiplication with arrays of same shape 
a = np.array([1.0, 2.0, 3.0]) 
b = np.array([2.0, 2.0, 2.0])

print a * b #produces  array of shape (3,) ([ 2.,  4.,  6.])

#Above exmaple using broadcasting 
a = np.array([1.0, 2.0, 3.0]) #array of shape (3,)
b = 2

print a * b # produces output same as above


#Adding one to each element of array using broadcasting
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
y = 1

print x +y #array([[ 2,  3,  4],
           #      [ 5,  6,  7],
           #      [ 8,  9, 10],
           #      [11, 12, 13]])

#Adding a vector to each row of matrix using broadcasting
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
y = np.array([1,2,3])
    
print x + y  #[[ 2,  4,  6],
             #[ 5,  7,  9],
             #[ 8, 10, 12],
             #[11, 13, 15]]
