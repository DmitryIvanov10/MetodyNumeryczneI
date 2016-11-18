# Lesson4, Tasks4-7

def print_matrix(matrix):
    """Print the n*n matrix"""
    print ()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]).rjust(6), end = '')
        print ()
    print ()

def matrix_multiplication(matrix1, matrix2):
    """Multiply two n*n matricies and returns the matrix of multiplication"""
    if len(matrix1[0]) != len(matrix2):
        return None
    else:
        result_matrix = []
        for i in range(len(matrix1)):
            result_matrix.append([])
            for j in range(len(matrix2[0])):
                x = 0
                for k in range(len(matrix1[0])):
                    x += matrix1[i][k] * matrix2[k][j]
                result_matrix[i].append(x)
        return result_matrix

def determinant(matrix):
    """Returns the determinant of the n*n matrix"""
    # check if matrix is squared
    new_matrix = [row[:] for row in matrix]
    if len(matrix[0]) != len(matrix):
        return None
        
    n = len(matrix)
    det = 1
    for i in range(n):
        # change the row if the element on the main diagonal is 0
        # return determinant = 0 if all lower rows are 0 up to main diagonal
        j = i
        while new_matrix[j][i] == 0 and j < n-1:
            j += 1
            if j == n:
                return 0
        if j != i:
            for k in range(i,n):
                # change rows, change the sign of the determinant
                new_matrix[i][k], new_matrix[j][k] = new_matrix[j][k], new_matrix[i][k]
            det *= -1

        # make first elements of lower rows equal to 0
        for j in range(i+1, n):
            if new_matrix[j][i] != 0: 
                a = new_matrix[i][i]
                b = new_matrix[j][i]
                for k in range(i, n):
                    new_matrix[j][k] -= new_matrix[i][k]*b/a

    # calculate determinant as a multiplication of diagonal elements
    for i in range(n):
        det *= new_matrix[i][i]
    
    # check for small uncertainties around 0
    if det == 0:
        return 0
        
    return det

def opposite_matrix(matrix):
    result_matrix = []
    for i in range(len(matrix)):
        result_matrix.append([])
        for j in range(len(matrix[0])):
            help_matrix = [row[:] for row in matrix]
            help_matrix.pop(i)
            for k in range(len(matrix)-1):
                help_matrix[k].pop(j)
            result_matrix[i].append((-1)**(i+j) * determinant(help_matrix) / determinant(matrix))
    for i in range(len(result_matrix)):
        for j in range(i+1, len(result_matrix[0])):
            result_matrix[i][j], result_matrix[j][i] = result_matrix[j][i], result_matrix[i][j]
    
    return result_matrix

def calculate_coefficients(A,b,name):
    # calculations x[] = A^(-1)[] * b[]
    answer = matrix_multiplication(opposite_matrix(A),b)
    
    #print initial data and answer
    print_matrix(A)
    print("     *     " + name + "     =")
    print_matrix(b)

    for i in range(len(A)):
        print("{}{} = {}".format(name, i, str(*answer[i]).rjust(4)))
    print ()
    return answer

# Task4
# initial data
A = [[0,0,2,1,2], [0,1,0,2,-1], [1,2,0,-2,0], [0,0,0,-1,1], [0,1,-1,1,-1]]
b = [[1],[1],[-4],[-2],[-1]]

print ("Task4")
print ()
calculate_coefficients(A,b,"x")

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
calculate_coefficients(A,b,"a") 

# Task6
# initial data
A = [[3.5,2.77,-0.76,1.8],[-1.8,2.68,3.44,-0.09],[0.27,5.07,6.9,1.61],[1.71,5.45,2.68,1.71]]
b = [[7.31],[4.23],[13.85],[11.55]]

print ("Task6")
print ()
x = calculate_coefficients(A,b,"x")

print ()
print ("det A = {}".format(determinant(A)))
print ()
print ("A[] * x[] = ")
print_matrix(matrix_multiplication(A,x))

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
    calculate_coefficients(A,b,"I")