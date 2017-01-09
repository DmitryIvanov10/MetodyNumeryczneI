# Lesson4, Tasks4-7

# Import own module 
import matrix_operations as m_op

# Task4
# initial data
A = [[0,0,2,1,2], [0,1,0,2,-1], [1,2,0,-2,0], [0,0,0,-1,1], [0,1,-1,1,-1]]
b = [[1],[1],[-4],[-2],[-1]]

print ("Task4")
print ()
m_op.calculate_coefficients(A,b,"x")

# Task5
# initial data
data = [[0,-1],[1,1],[3,3],[5,2],[6,-2]]
A = []
b = []
for i in range(len(data)):
    A.append([])
    b.append([])
    b[i].append(data[i][1])
    for j in range(len(data)):
        A[i].append(data[i][0] ** j)

print ("Task5")
print ()
m_op.calculate_coefficients(A,b,"a") 

# Task6
# initial data
A = [[3.5,2.77,-0.76,1.8],[-1.8,2.68,3.44,-0.09],[0.27,5.07,6.9,1.61],[1.71,5.45,2.68,1.71]]
b = [[7.31],[4.23],[13.85],[11.55]]

print ("Task6")
print ()
x = m_op.calculate_coefficients(A,b,"x")

print ()
print ("det A = {}".format(m_op.determinant(A)))
print ()
print ("A[] * x[] = ")
m_op.print_matrix(m_op.matrix_multiplication(A,x))

# Task7
# initial data
R = [5,10,20]

print ("Task7")
print ()

for i in range(len(R)):
    A = [[5,15,20],[5,-R[i],20+R[i]],[5+R[i],0,-R[i]]]
    b = [[220],[220],[220]]

    print ("Results for R = {}".format(R[i]))
    print ()
    m_op.calculate_coefficients(A,b,"I")

# Test task 
# initial data
A = [[1, 0, 3], [0, 0, 4], [0, 0, -2]]

print ()
print ("Test task")
print ()
print ("|A| = {}".format(m_op.determinant(A)))

