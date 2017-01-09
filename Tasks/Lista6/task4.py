# LEsson6, Task4

# import own module 
import matrix_operations as m_op

# import numpy module 
import numpy as np

# set initial data
B = []
x0 = []

for i in range(20):
    B.append([])
    x0.append([1])   
    for j in range(20):
        if i == j:
            B[i].append(round(0.025 * (i+1),3))
        elif j == i+1:
            B[i].append(5)
        else:
            B[i].append(0)

# print initial data 
print ("B:")
m_op.print_matrix(B)

print ("x0:")
m_op.print_matrix(x0)

# set first x for iterations
x = x0

# lowest index
k = 0
n = []

# main loop
for i in range(1,101):
    x = np.dot(B, x)
    n.append(np.linalg.norm(x)/np.linalg.norm(x0))
    if k == 0 and n[i-1] < 1:
        k = i

# print results
print ("k = {}".format(k))
