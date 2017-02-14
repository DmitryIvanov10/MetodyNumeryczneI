# Lesson10, Task5

# import own module 
import numerical_methods as num 

# import ln and constants e and pi
from math import log
from math import e
from math import pi

# initial data
def f(_x):
    return log(_x, e) / (_x**2 - 2*_x + 2)

a = 1
b = pi

# print results
for i in range(2,5,2):
    print ("Integral value for n = {}: I = {}".format(i, num.gauss_legendre_integral(f, a, b, i)))
    print ()
