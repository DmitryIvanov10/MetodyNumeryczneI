# Lesson7, Task2

# import cos and cosh
from math import cos
from math import cosh

# import function from own module
from numerical_methods import newton

# define function
def f(_x):
    return cos(_x)*cosh(_x) - 1

# calculations with Newton method
x, iterations = newton(f, 4.1)

# print results
print ("x = {}".format(x))
print ("f(x) = {}".format(f(x)))
print ()
print ("Number of iterations i = {}".format(iterations))
print ()
