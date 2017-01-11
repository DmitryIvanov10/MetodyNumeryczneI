# Lesson6, Task1

# import own module 
import matrix_operations as m_op

# import numpy module 
import numpy as np

# get machine epsilone
u = np.finfo(float).eps

# set initial data
A = m_op.hilbert_matrix(5)
b = m_op.transpose([[1,2,3,4,5]])

# print initial data 
print ("Matrix A:")
m_op.print_matrix(m_op.matrix_in_fractions(A))

print ()
print ("Matrix b:")
m_op.print_matrix(b)

# first calculations with LU method
x = m_op.solve_equations_by_LU(A,b)
r = m_op.subtract_two_dimensional_matricies(b, \
                     m_op.matrix_multiplication(A,x))

# print first results
print("First x:")
m_op.print_matrix(x)

print ("First r:")
m_op.print_matrix(r)

# number of iterations
iterations = 1

# main loop of the iterational answer corrections
while np.linalg.norm(r) > u * np.linalg.norm(np.dot(A,x)) and \
      np.linalg.norm(r) > u * np.linalg.norm(b):
    delta_x = m_op.matrix_multiplication(m_op.opposite_matrix(A),r)
    x = m_op.add_two_dimensional_matricies(x, delta_x)
    r = m_op.subtract_two_dimensional_matricies(b, \
                     m_op.matrix_multiplication(A,x))
    iterations += 1

# print results
print ("Number of iterations:")
print ("i = {}".format(iterations))
print ()

print ("Last r:")
m_op.print_matrix(r)

print ("Answer matrix x:")
m_op.print_matrix(x)

print ("Answer calculated with Gauss method:")
x = m_op.matrix_multiplication(m_op.opposite_matrix(A),b)
m_op.print_matrix(m_op.matrix_in_fractions(x))