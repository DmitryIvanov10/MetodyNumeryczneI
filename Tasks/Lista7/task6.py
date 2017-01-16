# Lesson7, Task6

# import function from own module
from numerical_methods import newton

# define functions
def y(_x):
    return _x**4 + (5 + 1j)*_x**3 - (8-5j)*_x**2 + (30-14j)*_x - 84

a = -10

# calculations with Newton method
x, iterations = newton(y, a)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = 0

# calculations with Newton method
x, iterations = newton(y, a)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = -5j

# calculations with Newton method
x, iterations = newton(y, a)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

a = 1j

# calculations with Newton method
x, iterations = newton(y, a)

# print results
print ("x = {}, y = {}".format(x, y(x)))
print ()

    
