# Lesson10, Task5

# import own module 
import numerical_methods as num 

# import numpy
import numpy as np

# import exp
from math import exp

# initial data
def f(_x):
    return (1 - _x**2)**(-0.5) * exp(-0.5 * _x**2)

a = -1
b = 1
n = 100

# print results
print ("Gauss-Legendre method:")
print ("Integral value for {} nods: I = {}".format(n, num.gauss_legendre_integral(f, a, b, n)))
print ()

