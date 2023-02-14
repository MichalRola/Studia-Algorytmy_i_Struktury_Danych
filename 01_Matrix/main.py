from matrix import Matrix


def transpose(item):
    rows, columns = Matrix.size(item)
    result = Matrix([columns, rows])
    for i in range(columns):
        for j in range(rows):
            result.matrix[i][j] = item.matrix[j][i]
    return result


a = Matrix([2], [[1, 0, 2], [-1, 3, 1]])
b = Matrix([2, 3], 1)
c = Matrix([3, 2], [[3, 1], [2, 1], [1, 0]])
transA = transpose(a)
z = a + b
y = z * c

print("Matrix A:")
print(a)
print("Transposition of the matrix A:")
print(transA)
print("Matrix B:")
print(b)
print("A + B =")
print(z)
print("Matrix C:")
print(c)
print("(A + B) * C =")
print(y)
