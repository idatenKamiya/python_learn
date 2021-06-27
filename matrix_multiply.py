p = int(input("enter the row number for matrix1: "))
q = int(input("enter the column number for matrix2: "))
n = int(input("enter the column number for matrix1/ row number of matrix2: "))

print("enter the elements for matrix1: ")
matrix1 = [[int(input()) for i in range(n)] for j in range (p)]
print("matrix1: ")
for i in range(p):
    for j in range(n):
        print(format(matrix1[i][j], "<5 "), end=" ")
    print("")

print("enter the elements for matrix2: ")
matrix2 = [[int(input()) for i in range(n)] for j in range (q)]
print("matrix2: ")
for i in range(n):
    for j in range(q):
        print(format(matrix2[i][j], "<5"), end=" ")
    print("")

result_matrix = [[0 for i in range(q)] for j in range(p)]
for i in range(p):
    for j in range(q):
        for k in range(n):
            result_matrix[i][j] = result_matrix[i][j] + matrix1[i][k] * matrix2[k][j]

print("result_matrix is: ")
for i in range(p):
    for j in range(q):
        print(format(matrix2[i][j],"<5"), end=" ")
    print("")