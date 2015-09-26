import numpy as np

'''Generate numpy array using in-built functions
'''
#Generates a 2 * 2 matrix of zeroes
a = np.zeros((2,2))

#Generates a 4 * 3 matrix of ones
b = np.ones((4,3))
'''Generate numpy array from python lists
'''
#example of numpy array of rank 1
rank1Array = np.array([1,2,3])

#example of numpy array of rank 2
rank2Array = np.array([[1,2,3],[4,5,6]])

'''Attributes of numpy array
'''

#ndim refers to number of dimension of a numpy array
print rank1Array.ndim    #prints 1
print rank2Array.ndim    #prints 2

#shape of an array is a tuple of integers giving the size of the array along each dimension.
print rank1Array.shape #print (3,)
print rank2Array.shape #print (2,3)

'''Array slicing
'''
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

#print ith row of a numpy array

print array[0] #prints the first row [1,2,3]
print array[2] #prints the third row [7,8,9]

#print ith column of a numpy array
print array[:,0] #prints the first column [1,4,7]
print array[:,2] #prints the third column [3,6,9]

#Transpose of a numpy array
array = np.array([[1,2],[3,4],[5,6]]) #array of shape 3,2
print array.T #prints transpose of array, having shape 2,3



''' Flattening and Reshaping
'''
x = np.array([ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ])

print x.flatten() #prints [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]

y = x.flatten()

print y.reshape(4,3) #converts y back to a (4,3) array
