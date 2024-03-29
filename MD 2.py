#Data Distribution is a list of all possible values, and how often each value occurs.
#A set of random numbers that follow a certain probability density function.
#for instances, A function that describes a continuous probability. i.e. probability of all values in an array.
#We can generate random numbers based on defined probabilities using the choice() method of the random module.
#The choice() method allows us to specify the probability for each value.
#The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.

from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

#in 2-d array
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
