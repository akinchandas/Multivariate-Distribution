#Logistic Distribution
#Logistic Distribution is used to describe growth.
#It's Used extensively in machine learning in logistic regression, neural networks etc.

from numpy import random
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

#loc - mean, where the peak is. Default 0.
#scale - standard deviation, the flatness of distribution. Default 1.
#size - The shape of the returned array.
