import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

#Basic mathematical operation involving numpy arrays are element-wise

#Element-wise sum
#[ [6 8],
#  [10 12]]
print x + y
print np.add(x, y)

#Element-wise difference
#[ [-4 -4],
#  [-4 -4]]
print x - y
print np.subtract(x, y)

# Element-wise product
#[ [5 12],
#  [21 32]]
print x * y
print np.multiply(x, y)

q = np.array([[1.0,2.0],[3.0,4.0]])
r = np.array([[5.0,6.0],[7.0,8.0]])

# Element-wise division
#[[ 0.2       ,  0.33333333],
# [ 0.42857143,  0.5       ]]
print q / r
print np.divide(q, r)

c = np.array([[1,2],[3,4]])
d = np.array([[5,6],[7,8]])
#Example of array dot product(i.e. matrix multiplication)
#[[19, 22],
# [43, 50]]
print c.dot(d)
print np.dot(c,d)

#sum operation on numpy array
x = np.array([[1,2],[3,4]])
print np.sum(x) #prints sum of all element of a numpy array 10
print np.sum(x, axis=0)  # Compute sum of each column; prints "[4 6]"
print np.sum(x, axis=1)  # Compute sum of each row; prints "[3 7]"


