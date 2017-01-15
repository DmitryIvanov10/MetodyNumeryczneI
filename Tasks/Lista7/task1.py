# Lesson7, Task1

# import functions from math 
from math import tan

# import pi 
from math import pi

# import own method 
import numerical_methods as num

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
x_bisection, bisection_iterations = num.bisection(f, sides[0], sides[1], epsilon)
if bisection_iterations != -1:
    print ()
    print ("x = {}".format(x_bisection))
    print ("f(x) = {}".format(f(x_bisection)))
    print ()
    print ("Number of iterations i = {}".format(bisection_iterations))
    print ()

# print results for Brent methods
print ("Brent method")
x_brent, brent_iterations = num.brent(f, sides[0], sides[1], epsilon)
if brent_iterations != -1:
    print ()
    print ("x = {}".format(x_brent))
    print ("f(x) = {}".format(f(x_brent)))
    print ()
    print ("Number of iterations i = {}".format(brent_iterations))
    print ()

# print results for secant methods
print ("Secant method")
x_secant, secant_iterations = num.secant(f, sides[0], sides[1], epsilon)
print ()
print ("x = {}".format(x_secant))
print ("f(x) = {}".format(f(x_brent)))
print ()
print ("Number of iterations i = {}".format(secant_iterations))
print ()

# print results for Newton methods
print ("Newton method")
x_newton, newton_iterations = num.newton(f, sides[0], epsilon)
print ()
print ("x = {}".format(x_newton))
print ("f(x) = {}".format(f(x_newton)))
print ()
print ("Number of iterations i = {}".format(newton_iterations))
print ()
