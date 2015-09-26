#NumPy

[Numpy](http://www.numpy.org/) is an open source extension module for Python. It is the core library for scientific computing in Python. 
It adds support to Python for large, multi-dimensional arrays and matrices. Besides that it supplies a large library of high-level mathematical functions to operate on these arrays. 

###Why use NumPy
Here is a python script which highlghts the benefits of numpy array over python list
```
'''Python script to compare perfomance of numpy array and python array

Here we are adding two arrays of 1 miilions items.
normal_version makes use of python lists while numpy_version makes use of numpy arrays

'''
import numpy
import time

def normal_version():
    t1 = time.time()
    X = range(1000000)
    Y = range(1000000)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    X = numpy.arange(1000000)
    Y = numpy.arange(1000000)
    Z = X + Y
    return time.time() - t1

print normal_version() #returns 0.160174846649
print numpy_version()  #return 0.00870800018311  
```
In the example above, the function with numpy array was 20 times as fast as the version involving the python list.
One reason for that is that numpy array is of homogeneous type, while python lists are arrays of pointer to objects even when all of them are of the same type. So, we get the benefits of locality of reference.   
Also, many Numpy operations are implemented in C, avoiding the general cost of loops in Python, pointer indirection and per-element dynamic type checking.

###Arrays in NumPy

Arrays are the central component of the module NumPy. A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the __rank__ of the array; the __shape__ of an array is a tuple of integers giving the size of the array along each dimension.

Refer to the [NumPy Array Example](https://github.com/joed7/fose_python/blob/master/numpy_example.py) for Numpy Array Syntax.

Some examples of numpy arrays and their attribumtes are as follows:

* `np.zeros((2,2))` generates a 2*2 array of zeroes
* `rank2Array = np.array([[1,2,3],[4,5,6]])` generates a 2*3 array 
* `rank2Array.ndim` returns the number of dimensions of a numpy array, 2 in this case
* `rank2Array.shape`returns the size of array along each dimension
* `rank2Array.T` return transpose of an array
* `np.array([ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ]).flatten()` returns all the elements in a single dimensional array
* `np.arange(12).reshape(4,3)` coverts one array into array of another size


###Matrix arthithmetic
Refer to the [Matrix arithmetic example](https://github.com/joed7/fose_python/blob/master/matrix-numpy.py) for python source code

Numpy module offers various methods to perform matrix arithmetic operations:  
For two numpy arrays `x` and `y`
* Matrix addition `np.add(x, y)`
* Matrix subtraction `np.subtract(x, y)`
* Matrix multiplication `np.multiply(x, y)`
* Matrix division `np.divide(x, y)`  
The command above operate element-wise on arrays.

Some other useful commands are
* Matrix dot product also matrix multiplication `np.dot(x,y)`
* Matrix sum of each column `np.sum(x,axis=0)`
* Matrix sum of each row `np.sum(x,axis=1)`
* Matrix sum of all element `np.sum(x)`

__Note__ In the exmaples shown in the [code](https://github.com/joed7/fose_python/blob/master/matrix-numpy.py), all of the matrices have the same shape. That does not necessarily have to be the case. Numpy has a concept of __Broadcasting__ which allows arithmetic operations between two matrix of different shape even they satisfy broadcasting criterion.
