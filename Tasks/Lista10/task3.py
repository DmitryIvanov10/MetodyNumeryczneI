# Lesson10, Task3

# import own module
import numerical_methods as num

# set initial data 
a = 0
b = 1

def f(_x):
    return (3*(1 + _x**(4/3)))**(-1)

# calculate and print results
integral = num.trapeze(f, a, b, 6)
print("I = {} for n = 6".format(integral))
print ()