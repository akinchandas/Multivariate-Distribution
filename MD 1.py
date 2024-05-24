#Random number does NOT mean a different number every time.
#Random means something that can not be predicted logically.


#the random module to work with random numbers.
from numpy import random
x = random.randint(100)
print(x)

#random module's rand() method returns a random float between 0 and 1.
from numpy import random
x = random.rand()
print(x)

#also
from numpy import random
x = random.rand(5)
print(x)

from numpy import random
x = random.rand(3, 5)
print(x)


#randint() method takes a size parameter where you can specify the shape of an array.
from numpy import random
x=random.randint(100, size=(5))
print(x)

#Generate a 2-D array with 3 rows,
#each row containing 5 random integers from 0 to 100:
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)


#The choice() method allows you to generate a random value based on an array of values.
#The choice() method takes an array as a parameter and randomly returns one of the values.
from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)

from numpy import random
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
