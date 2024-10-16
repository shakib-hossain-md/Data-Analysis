# To search an array, use the where() method

# Ex: Find the indexes where the value is 4
import numpy as np
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)
print(x)

# Ex: Find the indexes where the values are even

import numpy as np
arr = np.array([1,2,3,4,5,6,7])
x = np.where(arr%2 == 0)
print(x)

# Ex: Find the indexes where the values are odd

import numpy as np
arr = np.array([1,2,3,4,5,6,7])
x = np.where(arr%2 == 1)
print(x)


# Search Sorted
# The searchsorted() method is assumed to be used on sorted array

# Ex: Find the indexes  where the value should be inserted

import numpy as np
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,7)
print(x)

"""By default the left most index is returned, but we can give side = 'right' to return the right most index instead"""

# Ex: Find the indexes where the value 7 should be inserted from the right

import numpy as np
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,7,side='right')
print(x)

# Multiple Value

# Ex: Find the indexes where the values 2,4 and 6 should be inserted.

import numpy as np
arr = np.array([1,3,5,7])
x = np.searchsorted(arr,[2,4,6])
print(x)