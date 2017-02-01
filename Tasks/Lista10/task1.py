#Lesson10, Task1

# change own method for particular task
def trapeze(_f, _v, _p, _m = 2000, _eps = 0.0001):
    """Finds numerically definite integral of function in the interval [_a, _b]
    with precision _eps and returns the value of the integral"""
    """By default amount of nodes is 20"""

    # variable for the result value
    result = 0

    # main loop
    for i in range(len(_v) - 1):
        h = _v[i+1] - _v[i]
        result += 0.5 * (_f(_v[i], _p[i], _m) + _f(_v[i+1], _p[i+1], _m)) * h
    
    return result

# set function for the task 
def f(_vi, _pi, m = 2000):
    """Returns the value of the function in v = _v"""
    return m * _vi / _pi

# set initial data
v = [1.0, 1.8, 2.4, 3.5, 4.4, 5.1, 6.0]
p = [4700, 12200, 19000, 31800, 40100, 43800, 43200]
m = 2000

# calculate and print results
t = trapeze(f, v, p, m)
print("delta t = {}".format(t))
print ()