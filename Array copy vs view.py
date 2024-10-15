# Make a copy, change the original array and dispaly both array:

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


# Make a view, change the view, and display both arrays:

import  numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 43

print(arr)
print(x)


# Check if array owns its data

# Print the value of the base attribute to check if an array owns its data or not

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)