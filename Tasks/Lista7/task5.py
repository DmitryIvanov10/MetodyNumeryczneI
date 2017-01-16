# Lesson7, Task5

# import functions
from math import cos
from math import tan
from math import asin

# import function from own module
from numerical_methods import newton

# initial interval
a = 0
b = 1.5

# define functions
def y1(_x):
    return tan(_x) - 1

def y2(_x):
    return asin(cos(_x)/3)

def y(_x):
    return abs(y1(_x) - y2(_x))

# calculations with Newton method
x, iterations = newton(y, a)

# print results
print ("x = {}, y1 = {}, y2 = {}".format(x, y1(x), y2(x)))
print ()
