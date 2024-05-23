#Chi Square Distribution
#Chi Square distribution is used as a basis to verify the hypothesis.

from numpy import random
x = random.chisquare(df=2, size=(2, 3))
print(x)

#df - (degree of freedom).
#size - The shape of the returned array.
