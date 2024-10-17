# Generate a random integer from 0 to 100:
from numpy import random
x = random.randint(100)
print(x)


# Generate random float 0 to 1:
# The random module's rand() method returns a random float between 0 and 1
from  numpy import random
x = random.rand()
print(x)


# Generate random array
"""The randint() method takes a size parameter where you can specify the shape of an array"""

# Ex: Generate a 1D array containing 5 random integers from 0 to 100:
from numpy import random

x = random.randint(100,size=(5))
print(x)

# Ex: Generate a 2D array with 3 rows each row containing 5 random integers from 0 to 100.
from numpy import random
x = random.randint(100, size=(3,5))
print(x)

# Floats
"""The rand() method also allows you to specify the shape of the array"""
# Ex: Generate a 1D array with 3 rows, each row containing 5 random numbers.
from numpy import random

x = random.rand(3,5)
print(x)

# Generate random number from array
"""The choice() method allows you to generate a random value based on a array of values"""
from numpy import random
x = random.choice([3,5,7,9])
print(x)

# Ex: Generate a 2D array that consist of the values in the array parameter(3,5,7 and 9):
from numpy import random
x = random.choice([3,5,7,9], size=(3,5))
print(x)