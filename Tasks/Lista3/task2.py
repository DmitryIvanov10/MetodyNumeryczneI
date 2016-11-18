# Lesson3, Task2

from random import sample

# size of matricies
n = 3

def set_matrix(n, m):
    """Set random n*n matrix"""
    new_matrix = []
    for i in range(n):
        new_matrix.append(sample(range(10), m))
    return new_matrix

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
    
def print_matrix(matrix):
    """Print the matrix"""
    for i in range(len(matrix)):
        print (*matrix[i])
        print ()
      
# initial random matricies
matrix1 = set_matrix(n, n)
matrix2 = set_matrix(n, n)

# print print matrix multiplication
result_matrix = matrix_multiplication(matrix1,matrix2)

# print matricies
print_matrix(matrix1)
print ("  *")
print_matrix(matrix2)

# print result
if result_matrix != None:
    print ("  =")
    print_matrix(result_matrix)
else:
    print ()
    print ("You can't multiply those matricies")