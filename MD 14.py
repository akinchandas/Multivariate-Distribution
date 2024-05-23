#Zipf Distribution
#Zipf distributions are used to sample data based on zipf's law.

from numpy import random
x = random.zipf(a=2, size=(2, 3))
print(x)

#a - distribution parameter.
#size - The shape of the returned array.
