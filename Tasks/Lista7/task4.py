# Lesson7, Task4

# import ln
from math import log

# import exponent
from math import e

# import function from own module
from numerical_methods import newton

# initial data 
R = 8.31441
T0 = 4.44418
G = -10**5

# define function
def g(_T):
    return -R*_T*log((_T/T0)**2.5, e) - G

# calculations with Newton method
T, iterations = newton(g, T0)

# print results
print ("T = {} K".format(T))
print ("G(T) = {} J".format(g(T) + G))
print ()
print ("Number of iterations i = {}".format(iterations))
print ()