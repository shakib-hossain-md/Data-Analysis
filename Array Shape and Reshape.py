# ARRAY SHAPE

# Print the shape of an 2D array

import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

# Create ab array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimensions has value 4

import numpy as np
arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print("Shape of array:",arr.shape)


# ARRAY RESHAPE

# Reshape from 1D to 2D array

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)


# Reshape from 1D to 3D array
""" Convert the following 1-D array with 12 elements into a 3-D array.

The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:"""

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)

# Note: We can reshape into any shape, as long as the elements required for reshape are equal in both shape.


# Check if the return array a copy or view

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)
# The example above returns the original array, so it is a view.

# Unknown dimensions]
# pass -1 as the value and numpy will calculate this for you

# Conver 1D array with 8 elements to 3D array with 2x2 elements

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,-1)
print(newarr)



# Flattening array

"""Flattening array means converting a multidimensional array into 1D array
we can use reshape(-1) to do this"""

import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
newarr = arr.reshape(-1)
print(newarr)


"""Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy."""