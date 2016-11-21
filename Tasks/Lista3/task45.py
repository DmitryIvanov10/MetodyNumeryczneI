# Lesson2, Task4,5
# Version with profile
# Numpy is slower than the method shown to create values of x vector

from timeit import timeit
from numpy import arange
from numpy import size
import hotshot, hotshot.stats

def straight_polynom(value, coefficients):
    """Calculate polynom value with Horner algorythm
       Parameters are coefficients of the polynom and a value to calculate for"""
    polynom = 0
    for i,a in enumerate(coefficients):
        polynom += a * value**(len(coefficients)-1-i)
    return polynom

def calculate_polynoms_straight(x, coefficients):
    """Calculate polynoms for constant coefficients and x in range [-10,10] with dx = 0.0001"""
    for i in range(len(x)):
        straight_polynom(x[i], coefficients)
        
def horner_polynom(value, coefficients):
    """Calculate polynom value with Horner algorythm
       Parameters are coefficients of the polynom and a value to calculate for"""
    polynom = 0
    for a in coefficients:
        polynom = polynom * value + a
    return polynom

def calculate_polynoms_horner(x, coefficients):
    """Calculate polynoms for constant coefficients and x in range [-10,10] with dx = 0.0001"""
    for i in range(len(x)):
        horner_polynom(x[i], coefficients)

def main():
    # declare coefficients of the polynom (starting with highest power of the argument)
    coefficients = [6, 5, -13, 1, 1]

    # declare range and delta
    start = -10
    end = 10
    delta = 0.0001

    # create list of x values
    #x = arange(start, end, delta)
    i = start
    x = [i]
    while i <= end:
        i += delta
        x.append(i)
    
    calculate_polynoms_straight(x, coefficients)
    calculate_polynoms_horner(x, coefficients)
    
# run profiler and show stats    
profiler = hotshot.Profile ( "logfile.dat" )
profiler.run ( "main()" )
profiler.close ()

stats = hotshot.stats.load ( "logfile.dat" )
stats.print_stats (20)