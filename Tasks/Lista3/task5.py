# Lesson3, Task5
# numpy is commented since it's not working on my pc

from timeit import timeit
#from numpy import arange

# declare coefficients of the polynom (starting with highest power of the argument)
coefficients = [6, 5, -13, 1, 1]

# declare range and delta
start = -10
end = 10
delta = 0.0001

# create list of x values
#x = arange(start*10000, end*10000)
i = start
x = [i]
while i <= end:
    i += delta
    x.append(i)

def horner_polynom(value, coefficients):
    """Calculate polynom value with Horner algorythm
       Parameters are coefficients of the polynom and a value to calculate for"""
    polynom = 0
    for a in coefficients:
        polynom = polynom * value + a
    return polynom

def calculate_polynoms(x, coefficients):
    """Calculate polynoms for constant coefficients and x in range [-10,10] with dx = 0.0001"""
    for i in range(len(x)):
        horner_polynom(x[i], coefficients)

print ("Time of operations is {} ms".format(timeit("calculate_polynoms(x, coefficients)", 
setup = "from __main__ import calculate_polynoms, x, coefficients", number=10) * 100))