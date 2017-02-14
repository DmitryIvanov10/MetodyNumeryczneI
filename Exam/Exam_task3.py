# Lesson7, Task6

# import function from own module
from numerical_methods import newton

# import sin
from math import sin

# define functions
def y(_x):
    return sin(_x) - 0.125*_x

a = -8.5

# calculations with Newton method
x, iterations = newton(y, a, 0.000000000001)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = -7.0

# calculations with Newton method
x, iterations = newton(y, a, 0.000000000001)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = -4.0

# calculations with Newton method
x, iterations = newton(y, a, 0.000000000001)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = 1.0

# calculations with Newton method
x, iterations = newton(y, a, 0.000000000001)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = 2.0

# calculations with Newton method
x, iterations = newton(y, a, 0.000000000001)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = 6.0

# calculations with Newton method
x, iterations = newton(y, a, 0.000000000001)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = 9.0

# calculations with Newton method
x, iterations = newton(y, a, 0.000000000001)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()
