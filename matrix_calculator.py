def matrix_mult():
    matrix_A = []
    matrix_B = []

    user_input = input("Enter size of first matrix: ")
    print("Enter first matrix: ")
    matrix_size = [int(x) for x in user_input.split()]
    n = int(matrix_size[0])
    m = int(matrix_size[1])

    for _ in range(n):
        row_in = input()
        row = row_in.split()
        int_row = [float(x) for x in row]
        matrix_A.append(int_row)

    user_input = input("Enter size of second matrix: ")
    print("Enter second matrix: ")
    matrix_size = [int(x) for x in user_input.split()]
    n1 = int(matrix_size[0])
    m1 = int(matrix_size[1])
    for _ in range(n1):
        row_in = input()
        row = row_in.split()
        int_row = [float(x) for x in row]
        matrix_B.append(int_row)


    matrix = [[0 for i in range(m1)] for j in range(n)]
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_B)):
                matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    print("The result is: ")
    for row in matrix:
        print(*row)

def matrix_add():
    matrix_A = []
    matrix_B = []
    user_input = input("Enter size of first matrix: ")
    print("Enter first matrix: ")
    matrix_size = [int(x) for x in user_input.split()]
    n = int(matrix_size[0])
    m = int(matrix_size[1])

    for _ in range(n):
        row_in = input()
        row = row_in.split()
        int_row = [float(x) for x in row]
        matrix_A.append(int_row)

    user_input = input("Enter size of second matrix: ")
    print("Enter second matrix: ")
    matrix_size = [int(x) for x in user_input.split()]
    n1 = int(matrix_size[0])
    m1 = int(matrix_size[1])
    for _ in range(n1):
        row_in = input()
        row = row_in.split()
        int_row = [float(x) for x in row]
        matrix_B.append(int_row)

    if n == n1 and m == m1:
        for i in range(len(matrix_A)):
            for j in range(len(matrix_A[0])):
                matrix_A[i][j] += matrix_B[i][j]

        print("The result is: ")
        for row in matrix_A:
            print(*row)

    else:
        print("The operation cannot be performed.")

def input_matrix():
    matrix = []
    user_input = input("Enter size of matrix: ")
    matrix_size = [int(x) for x in user_input.split()]
    n = int(matrix_size[0])
    m = int(matrix_size[1])
    print("Enter matrix: ")

    for _ in range(n):
        row_in = input()
        row = row_in.split()
        int_row = [float(x) for x in row]
        matrix.append(int_row)
    return matrix

def constant_for_inverse(matrix, canstant):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = constant * matrix[i][j]

    print("The result is: ")
    for row in matrix:
        print(*row)



def constant_mult():
    matrix_A = []
    user_input = input("Enter size of matrix: ")
    print("Enter matrix: ")
    matrix_size = [int(x) for x in user_input.split()]
    n = int(matrix_size[0])
    m = int(matrix_size[1])

    for _ in range(n):
        row_in = input()
        row = row_in.split()
        int_row = [float(x) for x in row]
        matrix_A.append(int_row)

    constant = float(input("Enter constant: "))

    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[0])):
            matrix_A[i][j] = constant * matrix_A[i][j]

    print("The result is: ")
    for row in matrix_A:
        print(*row)


def transpose_1(matrix):
    result = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[j][i] = matrix[i][j]
    return result

def transpose():


    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

    choice = int(input("Your choice: "))
    matrix_A = []
    user_input = input("Enter size of matrix: ")
    print("Enter matrix: ")
    matrix_size = [int(x) for x in user_input.split()]
    n = matrix_size[0]
    m = matrix_size[1]

    result = [[0 for i in range(n)] for j in range(m)]

    for _ in range(n):
        row_in = input()
        row = row_in.split()
        int_row = [float(x) for x in row]
        matrix_A.append(int_row)

    if choice == 1:
        for i in range(len(matrix_A)):
            for j in range(len(matrix_A[0])):
                result[j][i] = matrix_A[i][j]
        print("The result is: ")
        for row in result:
            print(*row)

    elif choice == 2:
        for i in range(len(matrix_A) - 1, -1, -1):
            for j in range(len(matrix_A[0]) - 1, -1, -1):
                result[(len(matrix_A[0]) - 1) - j][(len(matrix_A) - 1) - i] = matrix_A[i][j]
        print("The result is: ")
        for row in result:
            print(*row)

    elif choice == 3:
        for i in range(len(matrix_A[0])):
            for j in range(len(matrix_A)):
                result[j][(len(matrix_A[0]) - 1) - i] = matrix_A[j][i]
        print("The result is: ")
        for row in result:
            print(*row)

    elif choice == 4:
        for i in range(len(matrix_A[0])):
            for j in range(len(matrix_A)):
                result[(len(matrix_A[0]) - 1) - i][j] = matrix_A[i][j]
        print("The result is: ")
        for row in result:
            print(*row)

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    elif len(m) == 1 and len(m[0]) == 1:
        return m[0][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrix_of_cofactors(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    elif len(m) == 1 and len(m[0]) == 1:
        return m[0][0]

    cofactor_matrix =[[0 for j in range(len(m))] for i in range(len(m))]
    for c in range(len(m)):
        for j in range(len(m)):
            cofactor_matrix[c][j] = ((-1)**(c + j))*getMatrixDeternminant(getMatrixMinor(m,c,j))
    return cofactor_matrix


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    user_choice = int(input("Your choice: "))
    if user_choice == 1:
        matrix_add()
    elif user_choice == 2:
        constant_mult()
    elif user_choice == 3:
        matrix_mult()
    elif user_choice == 4:
        transpose()
    elif user_choice == 5:
        matrix = []
        user_input = input("Enter size of matrix: ")
        print("Enter matrix: ")
        matrix_size = [int(x) for x in user_input.split()]
        n = int(matrix_size[0])
        m = int(matrix_size[1])

        for _ in range(n):
            row_in = input()
            row = row_in.split()
            int_row = [float(x) for x in row]
            matrix.append(int_row)
        print("The result is: ")
        print(getMatrixDeternminant(matrix))
    elif user_choice == 6:
        matrix = input_matrix()
        det = getMatrixDeternminant(matrix)
        matrix_of_cofactors = getMatrix_of_cofactors(matrix)
        adjoin = transpose_1(matrix_of_cofactors)
        if det == 0:
            print("The matrix does not have an inverse")
        else:
            constant = 1 / det
            constant_for_inverse(adjoin, constant)
    elif user_choice == 0:
        break
