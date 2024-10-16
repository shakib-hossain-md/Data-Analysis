# Checking the data type of an array
"""The NumPy array object has a property called dtype that returns the data type of the array"""

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype)

# Get the data type of an array containing string

import numpy as np
arr = np.array(["apple","banana","cherry"])
print(arr)
print(arr.dtype)

# For i,u,f,S and U we can define size as well

# Create an array with the data type 4 bytes integer
import numpy as np
arr = np.array([1,2,3,4,5], dtype='i4')
print(arr)
print(arr.dtype)


# Converting data type on existing arrays
"""The best way to change the data type of existing array, is to make a copy of the array with the astype() method"""

# Change data type from float to integer by using 'i' as parameter value

import numpy as np
arr = np.array([1.1,2.1,3.1])

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)


# Change the data type from integer to boolean.

import numpy as np
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)