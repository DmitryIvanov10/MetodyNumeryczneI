# Lesson2, Task7

from random import random
from math import log10

a = c = 1

# Part a
# Sometimes gives 0 for the value of x1 (when the difference between b and sqrt is small)
for i in range(100):
    
    b = random() * (10 ** 7.4 + 10 ** 8.5) - 10 ** 7.4

    x1 = (1 / (2*a)) * (-b + (b ** 2 - 4*a*c) ** 0.5)
    x2 = (1 / (2*a)) * (-b - (b ** 2 - 4*a*c) ** 0.5)

    print ("x1 = {}, x2 = {}".format(x1, x2))

print ()

# Part b
for i in range(100):
    
    b = random() * (10 ** 7.4 + 10 ** 8.5) - 10 ** 7.4

    x1 = (1 / (2*a)) * (-b - (b ** 2 - 4*a*c) ** 0.5)
    x2 = c / (a * x1)

    print ("x1 = {}, x2 = {}".format(x1, x2))
