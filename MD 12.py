#Rayleigh Distribution
#Rayleigh distribution is used in signal processing.

from numpy import random
x = random.rayleigh(scale=2, size=(2, 3))
print(x)

#scale - (standard deviation) decides how flat the distribution will be default 1.0).
#size - The shape of the returned array.
