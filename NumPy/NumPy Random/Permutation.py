# Random permutation of elements
"""The random module provides two methods for this: shuffle() and permutation()"""

# Shuffling array
"""Shufle means changing arrangement of elements in plae"""
# Ex: Randomly shuffle elements of following array

from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

# Note: The shuffle() method make changes to the original array.

# Generating permutation of arrays
# Ex: Generate a random permutation of elements of following array

from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])
print(random.permutation(arr))

# Note: The permutation() method returns a re-arranged array(and leaves the original array un-changed)