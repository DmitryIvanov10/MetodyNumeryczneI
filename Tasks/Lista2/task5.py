# Lesson2, Task5

from math import exp
from math import factorial
from numpy import arange
import matplotlib.pyplot as plt

# Plot with MatPlotLib by x and y
def plotWithMatplotlib(x, y, name):
    plt.plot(x,y)

    plt.ylabel(name)
    plt.xlabel('x')

# A function for exponent
def exponent(x, N):
    sum = 0
    partSums = []
    for i in range (N):
        sum += (x ** i) / factorial(i)
        partSums.append(exp(x) - sum)
    return partSums

# Amount of partial sums variables
N = 60
NValues = arange(N)

x = 10
plotWithMatplotlib(NValues, exponent(x, N), 'Exp uncertainty for |x| = 10')

x = -10
plotWithMatplotlib(NValues, exponent(x, N), 'Exp uncertainty for |x| = 10')

plt.show()
plt.clf()

x = 2
plotWithMatplotlib(NValues, exponent(x, N), 'Exp uncertainty for |x| = 2')

x = -2
plotWithMatplotlib(NValues, exponent(x, N), 'Exp uncertainty for |x| = 2')

plt.show()