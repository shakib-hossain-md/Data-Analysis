# The array object of NumPy is called ndarray.

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# Use a tuple to create NumPy array
import numpy as np
arr = np.array((1,2,3,4,5))
print(arr)

# 0-D array

import numpy as np
arr = np.array(43)
print(arr)


# 1-D array
"""An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array."""

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

# 2-D array
"""An array that has 1-D arrays as its elements is called a 2-D array.
* NumPy has a whole sub-module dedicated towards matrix operations called numpy.mat"""

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

# 3-D array
"""An array that has 2-D arrays as its elements is called a 2-D array."""
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)


# Check number of dimensions of an array
"""NumPy arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have."""

import numpy as np
a = np.array(43)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional array
"""An array can have any numbers of dimensions when the array is created, you can define the number of dimensions by using the ndmin argument"""

import numpy as np
arr = np.array([1,2,3,4,5], ndmin=5)
print(arr)
print("Number of Dimensions:", arr.ndim)