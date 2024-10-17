"""Data distribution is a list of possible values and how often each value occurs"""

# Random Distribution
"""A random distribution is a set of random numbers that follow a certain probability density function.
Probability density function: A function that describes a continous probability(probability of all values in an array)"""

# Ex: Generate a  1-D array containing 100 values, where each value has to be 3,5,7 or 9.
"""
The probability for the value 3 is set to be 0.1
The probability for the value 5 is set to be 0.3
The probability for the value 7 is set to be 0.6
The probability for the value 9 is set to be 0.0"""

from numpy import random
x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100))
print(x)

# Note: The sum of the probability number is should be 1.

# Ex: Same example above,but return a 2-D array with 3 rows,each containing 5 values.

from numpy import random
x = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0], size=(3,5))
print(x)