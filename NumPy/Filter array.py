"""If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array."""

# Ex: Create an array from the elements on index 0 to 2

import numpy as np
arr = np.array([41,42,43,44])
x = [True,False,True,False]

newarr = arr[x]
print(newarr)

# Creating the filter array
# Ex: Create a filter array that will return only higher value than 42

import numpy as np
arr = np.array([41,42,43,44])
filter_arr = []

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newrr = arr[filter_arr]

print(filter_arr)
print(newarr)


# Ex: Create a filter array that will return only even elements from the original array

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
filter_arr = []

for element in arr:
  if element%2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Creating filter direct from array
import numpy as np
arr = np.array([41,42,43,44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# For Even number

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
filter_arr = arr%2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)