# Join 2 arrays

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))
print(arr)


# Join 2D array along rows: (axis = 1)

import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

arr = np.concatenate((arr1,arr2), axis=1)
print(arr)


# Joining Arrays using stack function

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.stack((arr1,arr2), axis=1)
print(arr)

# Stacking along Rows
# NumPy provides a helper function hstack() to stack along rows

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.hstack((arr1,arr2))
print(arr)


# Stacking along columns
# NumPy provides a helper fucntion vstack() to stack along columns

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.vstack((arr1,arr2))
print(arr)

# Stacking along hight
# NumPy provides a helper fucntion dstack() to stack along hight

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.dstack((arr1,arr2))
print(arr)