# Lesson7, Task3

# import ln
from math import log

# import exponent
from math import e

# import function from own module
from numerical_methods import newton

# initial data 
u = 2510
M0 = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81
vs = 335

# define function
def v(_t):
    return u*log(M0/(M0-m*_t), e) - g*_t - vs

# calculations with Newton method
t, iterations = newton(v, 0)

# print results
print ("t = {} s".format(t))
print ("v(t)= {} m/s".format(v(t) + vs))
print ()
print ("Number of iterations i = {}".format(iterations))
print ()