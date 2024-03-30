#Normal Distribution
#The Normal Distribution is one of the most important distributions.

#The probability distribution of many events,
#we are going to use the random.normal() method to get a Normal Data Distribution.
#With three parameters:
#loc - (Mean) where the peak of the bell exists.
#scale - (Standard Deviation) how flat the graph distribution should be.
#size - The shape.

from numpy import random
x = random.normal(size=(2, 3))
print(x)

#A random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:

from numpy import random
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

