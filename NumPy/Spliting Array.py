# We use array_split() for spliting array
# Ex: Split the array into 3 part 
import numpy as np
arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,3)
print(newarr)

# If the array has less elements than required, it will adjust from the end accordingly

import numpy as np
arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,4)
print(newarr)

# Split into arrays
# Ex : Access the split array

import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# Note: Similar alternate to vstack() and dstack() are available as vsplit() and dsplit().