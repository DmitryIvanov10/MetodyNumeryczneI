# Lesson2, Task2

# number in decimal 
number_in_decimal = 1.7

# number from IEEE
number_from_IEEE = (1 + 2**(-1) + 2**(-3) + 2**(-4) + 2**(-7) + 2**(-8) +
                    2**(-11) + 2**(-12) + 2**(-15) + 2**(-16) + 2**(-19) +
                    2**(-20) + 2**(-23)) * 2**0

# absolute error
absolute_error = abs(number_in_decimal - number_from_IEEE)

# relative error
relative_error = absolute_error/abs(number_in_decimal)

# print results
print ("Absolute error = {}".format(absolute_error))
print ()
print ("Relative error = {}".format(relative_error))