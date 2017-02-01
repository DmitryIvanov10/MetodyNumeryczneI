# Lesson10, Task2

# import cos 
from math import cos

# import own module
import numerical_methods as num

# set initial data 
a = -1
b = 1

def f(_x):
    return cos(2 * cos(_x)**(-1)) 

# calculate and print results
integral = num.simpson(f, a, b, 3)
print("I = {} for n = 3".format(integral))
print ()

integral = num.simpson(f, a, b, 5)
print("I = {} for n = 5".format(integral))
print ()

integral = num.simpson(f, a, b, 7)
print("I = {} for n = 7".format(integral))
print ()
