#Uniform Distribution
#Used to describe probability where every event has equal chances of occuring.

from numpy import random
x = random.uniform(size=(2, 3))
print(x)

#a - lower bound - default 0 .0.
#b - upper bound - default 1.0.
#size - The shape of the returned array.
