# Lesson7, Task1

# import functions from math 
from math import tan
from math import log

# import pi 
from math import pi

def g(_f, a, b, c):
    """Returns value of the function depending on a,b,c"""
    return -( a*_f(b)*_f(c)*(_f(b)-_f(c)) + \
              b*_f(c)*_f(a)*(_f(c)-_f(a)) + \
              c*_f(a)*_f(b)*(_f(a)-_f(b)) ) / \
            ( (_f(a)-_f(b)) * (_f(b)-_f(c)) * (_f(c)-_f(a)) )

def bisection(_f, _a, _b, _eps):
    # check if signs on two sides are different
    if _f(_a) * _f(_b) > 0:
        print ()
        print ("No zero places.") 
        print ()
        return 0, -1

    # iteration parameteres
    run = True
    iterations = 0

    while run:
        # calculate iteration
        iterations += 1    

        # devide interval into half
        c = (_a + _b) / 2

        # check if 0 on the division point
        if abs(_f(c)) < _eps:
            x = c
            run = False
            return x, iterations

        # change sides depending on the value of the function in the middle of the interval
        if _f(c) * _f(_a) > 0:
            _a = c
        else:
            _b = c

def brent(_f, _a, _b, _eps):
    # check if signs on two sides are different
    if _f(_a) * _f(_b) > 0:
        print ()
        print ("No zero places.") 
        print ()
        return 0, -1

    # iteration parameteres
    run = True
    iterations = 0

    while run:
        # calculate iteration
        iterations += 1    

        # devide interval
        if  iterations == 1 or x > _b or x < _a:
            c = (_a + _b) / 2
        elif abs(_f(c)) < _eps:
            run = False
            return x, iterations
        else:
            c = x 

        # calculate possible x for Brent method (parabola from three points)
        x = g(_f, _a, _b, c) 

        # change sides depending on the value of the function in the middle of the interval
        if _f(c) * _f(_a) < 0:
            _b = c
        else:
            _a = c     

# constant for accuracy of calculations
epsilon = 0.00001

# initial data 
sides = [1.8, 2.05]

def f(x):
    """Returns value of the function in x"""
    return tan(pi - x) - x

# print initial data
print ("f(x) = tg(Pi - x) - x")
print ()

print ("Interval [{}, {}]".format(sides[0], sides[1]))
print ()

print ("Calculating with precision epsilon = {}".format(epsilon))
print ()

# print results for bisection methods
print ("Bisection method")
x_bisection, bisection_iterations = bisection(f, sides[0], sides[1], epsilon)
if bisection_iterations != -1:
    print ()
    print ("x = {}".format(x_bisection))
    print ("f(x) = {}".format(f(x_bisection)))
    print ()
    print ("Number of iterations i = {}".format(bisection_iterations))
    print ()

# print results for Brent methods
print ("Brent method")
x_brent, brent_iterations = brent(f, sides[0], sides[1], epsilon)
if brent_iterations != -1:
    print ()
    print ("x = {}".format(x_brent))
    print ("f(x) = {}".format(f(x_brent), 6))
    print ()
    print ("Number of iterations i = {}".format(brent_iterations))
    print ()
