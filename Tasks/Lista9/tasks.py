# Lesson9

# import functions from math
from math import exp

# Task1

# calculated coefficients
a1 = 3.61372
b1 = 0.544249

# function in task1
def f1(_x):
    return a1 * exp(_x*b1)

# Task2

# calculated coefficients
a2 = -1.2005 * 10**(-6) 
b2 = 0.000376048
c2 = -0.0405887
d2 = 1.79758

# Task3

# calculated coefficients
a3l = 9.43854
b3l = -6.1899

a3s = 1.36149
b3s = 2.88736
c3s = -0.0405681

# function in task1
def f2(_x):
    return a2*_x**3 + b2*_x**2 + c2*_x + d2

# print results
# Task1
print ("Task1")
print ("Coefficients for f(x) = a*exp(x*b)")
print ()
print ("a = {} \nb = {}".format(a1, b1))
print ()

# Task2
print ("Task2")
print ("Coefficients for f(x) = a*x^3 + b*x^2 + c*x + d")
print ()
print ("a = {} \nb = {} \nc = {} \nd = {}".format(a2, b2, c2, d2))
print ()
print ("mk(10) = {} * 10^(-3) m^2/s".format(f2(10)))
print ("mk(30) = {} * 10^(-3) m^2/s".format(f2(30)))
print ("mk(60) = {} * 10^(-3) m^2/s".format(f2(60)))
print ("mk(90) = {} * 10^(-3) m^2/s".format(f2(90)))

# Task1
print ("Task3")
print ("Coefficients for f(x) = a*x + b")
print ()
print ("a = {} \nb = {}".format(a3l, b3l))
print ()
print ("Coefficients for f(x) = a*x^2 + b*x + c")
print ()
print ("a = {} \nb = {} \nc = {}".format(a3s, b3s, c3s))
print ()