#Multinomial Distribution
#Multinomial distribution is a generalization of binomial distribution.
#It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

#n - number of possible outcomes.
#pvals - list of probabilties of outcomes.
#size - The shape of the returned array.
