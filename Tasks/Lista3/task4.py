# Lesson2, Task4
# Version with timeit

from timeit import timeit
from numpy import arange
from numpy import size

# declare coefficients of the polynom (starting with highest power of the argument)
coefficients = [6, 5, -13, 1, 1]

# declare range and delta
start = -10
end = 10
delta = 0.0001

# create list of x values
x = arange(start, end, delta)
"""i = start
x = [i]
while i <= end:
    i += delta
    x.append(i)"""

def straight_polynom(value, coefficients):
    """Calculate polynom value with Horner algorythm
       Parameters are coefficients of the polynom and a value to calculate for"""
    polynom = 0
    for i,a in enumerate(coefficients):
        polynom += a * value**(len(coefficients)-1-i)
    return polynom

def calculate_polynoms(x, coefficients):
    """Calculate polynoms for constant coefficients and x in range [-10,10] with dx = 0.0001"""
    for i in range(len(x)):
        straight_polynom(x[i], coefficients)

# print results - time of the operations using timeit
print ("Time of operations is {} ms".format(timeit("calculate_polynoms(x, coefficients)", 
setup = "from __main__ import calculate_polynoms, x, coefficients", number=1) * 1000))