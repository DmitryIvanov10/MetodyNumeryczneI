# Lesson2, Task6

x = 9.8 ** 201
y = 10.2 ** 199

def z1(x,y):
    return (x ** 2 + y **2) ** (0.5)

def z2(x,y):
    return y * ( ((x/y) ** 2 + 1) ** (0.5) )

# Can't put such big numbers to the second power
#print ("First method {}".format(z1(x,y)))

# Can put a division of big numbers to the second power
print ("Second method {}".format(z2(x,y)))