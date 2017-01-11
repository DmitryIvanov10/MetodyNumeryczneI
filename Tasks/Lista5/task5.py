# Lesson5, Task5

# Import own module 
import matrix_operations as m_op

from fractions import Fraction

# define minimal determinant
epsilon = 10 ** (-6)

# initial data 
A = [[1,  3, -9,  6, 4], \
     [2, -1,  6,  7, 1], \
     [3,  2, -3, 15, 5], \
     [8, -1,  1,  4, 2], \
     [11, 1, -2, 18, 7]]

# calculate determinant and opposite matrix
A_op = m_op.opposite_matrix(A)
det_A = m_op.determinant(A)

# print results
print ("Matrix A:")
print ()
m_op.print_matrix(A)

print ()

print ("|A| = {}".format(det_A))
print ()

print ("Matrix opposite to A:")
print ()

det_A = Fraction(det_A).limit_denominator()

if det_A == 0:
    print ("No opposite matrix.")
elif det_A > epsilon:
    m_op.print_matrix(A_op)
else:
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - 1):
            print ("A_op[{}][{}] = {}".format(i+1, j+1, A_op[i][j]))


