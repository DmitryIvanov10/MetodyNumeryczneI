# Lesson7, Task1

# import functions from math 
from math import tan

# import pi 
from math import pi

def g(_f, a, b, c):
    """Returns value of the function depending on a,b,c"""
    return -( a*_f(b)*_f(c)*(_f(b)-_f(c)) + \
              b*_f(c)*_f(a)*(_f(c)-_f(a)) + \
              c*_f(a)*_f(b)*(_f(a)-_f(b)) ) / \
            ( (_f(a)-_f(b)) * (_f(b)-_f(c)) * (_f(c)-_f(a)) )

def bisection(_f, _a, _b, _eps = 0.0001):
    """Finds zero place of function _f if possible in interval [_a, _b] 
    with precision _eps by bisection method""" 
    # check if signs on two sides are different
    if _f(_a) * _f(_b) > 0:
        print ()
        print ("No zero places.") 
        print ()
        return 0, -1

    # iteration parameteres
    iterations = 0

    while True:
        # calculate iteration
        iterations += 1    

        # devide interval into half
        c = (_a + _b) / 2

        # check if 0 on the division point
        if abs(_f(c)) < _eps:
            x = c
            return x, iterations

        # change sides depending on the value of the function in the middle of the interval
        if _f(c) * _f(_a) > 0:
            _a = c
        else:
            _b = c

        if iterations > 1/_eps:
            print ("No zero places.")
            return 0, -1

def brent(_f, _a, _b, _eps = 0.0001):
    """Finds zero place of function _f if possible in interval [_a, _b] 
    with precision _eps by Brent method""" 
    # check if signs on two sides are different
    if _f(_a) * _f(_b) > 0:
        print ()
        print ("No zero places.") 
        print ()
        return 0, -1

    # iteration parameteres
    iterations = 0

    while True:
        # calculate iteration
        iterations += 1    

        # devide interval
        if  iterations == 1 or x > _b or x < _a:
            c = (_a + _b) / 2
        elif abs(_f(c)) < _eps:
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

def secant(_f, _a, _b, _eps = 0.0001):
    """Finds zero place of function _f if possible in interval [_a, _b] 
    with precision _eps by secant method""" 

    # iteration parameteres
    iterations = 0

    while True:
        # calculate iteration
        iterations += 1  

        # find next element and reset previous
        _a, _b = _b, _b - _f(_b) * (_b - _a) / (_f(_b) - _f(_a))

        if (abs(_f(_b)) < _eps):
            return _b, iterations

def newton(_f, _a, _eps = 0.0001):
    """Finds zero place of function _f if possible from x0 = _a 
    with precision _eps by Newton method""" 

    # iteration parameteres
    iterations = 0

    while True:
        # calculate iteration
        iterations += 1  

        # find next element and reset previous
        _a = _a - _f(_a) * _eps / (_f(_a + _eps) - _f(_a))

        if (abs(_f(_a)) < _eps):
            return _a, iterations

# constant for accuracy of calculations
epsilon = 0.0001

# initial data 
sides = [-4, -1.9]

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

# print results for secant methods
print ("Secant method")
x_secant, secant_iterations = secant(f, sides[0], sides[1], epsilon)
print ()
print ("x = {}".format(x_secant))
print ("f(x) = {}".format(f(x_brent), 6))
print ()
print ("Number of iterations i = {}".format(secant_iterations))
print ()

# print results for Newton methods
print ("Newton method")
x_newton, newton_iterations = newton(f, sides[0], epsilon)
print ()
print ("x = {}".format(x_newton))
print ("f(x) = {}".format(f(x_newton), 6))
print ()
print ("Number of iterations i = {}".format(newton_iterations))
print ()
