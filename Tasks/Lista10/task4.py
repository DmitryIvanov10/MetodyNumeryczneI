# Lesson10, Task4

# import sin 
from math import sin
from math import pi

from numerical_methods import grad_to_rad

# change own method for particular task
def simpson(_f, _a, _b, _const, n = 20, _eps = 0.0001):
    """Finds numerically definite integral of function in the interval [_a, _b]
    with precision _eps and returns the value of the integral"""
    """By default amount of nodes is 20"""
    
    # calculate step
    h = (_b - _a) / n  

    # variable for the result value
    result = 0

    # main loop
    for i in range(n+1):
        # first or last element
        if i==0 or i==n:
            result += _f(_a, _const)
        # odd element
        elif i % 2 == 1:
            result += 4 * _f(_a, _const)
        # even element    
        else:
            result += 2 * _f(_a, _const)
        # do step
        _a += h

    return result * h / 3

# define function for the task
def h(_theta, _theta0):
    """Define own function for h(theta, theta1)"""
    return 1 / (1 - sin(grad_to_rad(_theta0)/2)**2 * sin(_theta)**2)**(0.5) 

# set initial data 
a = 0
b = pi / 2

# calculate and print results
theta0 = 0
integral = simpson(h, a, b, theta0)
print("h({}) = {} Pi for n = 20".format(theta0, integral/pi))
print ()

# calculate and print results
theta0 = 15
integral = simpson(h, a, b, theta0)
print("h({}) = {} Pi for n = 20".format(theta0, integral/pi))
print ()

# calculate and print results
theta0 = 30
integral = simpson(h, a, b, theta0)
print("h({}) = {} Pi for n = 20".format(theta0, integral/pi))
print ()

# calculate and print results
theta0 = 45
integral = simpson(h, a, b, theta0)
print("h({}) = {} Pi for n = 20".format(theta0, integral/pi))
print ()

# calculate and print results
theta0 = 60
integral = simpson(h, a, b, theta0)
print("h({}) = {} Pi for n = 20".format(theta0, integral/pi))
print ()

# calculate and print results
theta0 = 75
integral = simpson(h, a, b, theta0)
print("h({}) = {} Pi for n = 20".format(theta0, integral/pi))
print ()

# calculate and print results
theta0 = 90
integral = simpson(h, a, b, theta0)
print("h({}) = {} Pi for n = 20".format(theta0, integral/pi))
print ()