# Iterating means going through elements one by one.

# Ex: Iterate on the elements of following 1D array.

import numpy as np
arr = np.array([1,2,3])
for x in arr:
  print(x)


"""To return the actual values, the scalars we have to iterate the arrays in each dimension."""

# Ex: Iterate on each scalar element of 2D array.

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
  for y in x:
    print(y)

# Iterate 3D array

import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)

# Iterating arrays using nditer()
"""The function nditer() is helping function that can be used from very basic to very advanced iteration."""

import numpy as np
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
  print(x)


# Iterating arays with different data type
"""We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']."""


import numpy as np
arr = np.array([1,2,3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes='S'):
  print(x)

# Iterating with different step size.

# Ex: Iterate through every scalar element of 2D array skipping 1 element.

import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

# Enumerate Iteration using ndneumerate()

"""Eneumerate means maintaing sequence number of something one by one"""

#  For 1D array

import numpy as np
arr = np.array([1,2,3])
for idx,x in np.ndenumerate(arr):
  print(idx, x)

# for 2D array

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for idx,x in np.ndenumerate(arr):
  print(idx, x)