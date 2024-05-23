#Poisson Distribution is a Discrete Distribution.
#This distribution estimates how many times an event can happen in a specified time

from numpy import random
x = random.poisson(lam=2, size=10)
print(x)

#lam - rate or known number of occurrences e.g. 2 for above problem.
#size - The shape of the returned array.
