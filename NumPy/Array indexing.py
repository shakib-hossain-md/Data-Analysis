"""Array indexing is the same as accessing an array element.
You can access an array element by referring to its index number."""

# Get the first element from the following array
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[0])

#  ACCESS 2-D ARRAY
"""To access element from 2-D array we can use comma to seperated integers representing the dimensions and the index number of the element.
"""
# Access the element on the first row second column.

import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2nd element on 1st row:", arr[0,1])


# ACESS 3-D ARRAY

# Access the 3rd element of the second array of 1st array.\

import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2])

# Explanation:
"""The 1st number represents the 1st dimension, which contain 2 arrays.
The 2nd number repesents the 2nd dimension,which also contain 2 arrays.
The 3rd number represents the 3rd dimension, which contains three values.
and the value of index 2 is 6."""

# Negetive indexing

# Print the last number of the 2nd dim:
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Last element of 2nd dim:", arr[1,-1])