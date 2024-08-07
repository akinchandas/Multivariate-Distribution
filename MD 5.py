#888888888888888888888
#Binomial Distribution
#AKA a Discrete Distribution.
#The outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

#With three parameters:
#n - number of trials.
#p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
#size - The shape of the returned array.

from numpy import random
x = random.binomial(n=10, p=0.5, size=10)
print(x)


#The distribution is defined at separate set of events, e.g. a coin toss's result is discrete,
#as it can be only head or tails whereas height of people is continuous as it can be 170, 170.1, 170.11 and so on.
