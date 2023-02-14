class Matrix:
    def __init__(self, dims, data=0):
        if isinstance(data, list):
            self.matrix = [data[i] for i in range(dims[0])]
        else:
            if len(dims) == 1:
                print("Not enough dimensions given.")
                raise ValueError
            else:
                self.matrix = [[data] * dims[1] for _ in range(dims[0])]

    def __add__(self, object2):
        rows_self, columns_self = Matrix.size(self)
        rows_object2, columns_object2 = Matrix.size(object2)

        if rows_self == rows_object2 and columns_self == columns_object2:
            result = Matrix([rows_self, columns_self])
            for i in range(rows_self):
                for j in range(columns_self):
                    result.matrix[i][j] = self.matrix[i][j] + object2.matrix[i][j]
            return result
        else:
            print("Matrices aren't the same size.")
            return 1

    def __mul__(self, object2):
        rows_self, columns_self = Matrix.size(self)
        rows_object2, columns_object2 = Matrix.size(object2)

        if columns_self == rows_object2:
            result = Matrix([rows_self, columns_object2])
            for i in range(rows_self):
                for j in range(columns_object2):
                    for k in range(rows_object2):
                        result.matrix[i][j] += self.matrix[i][k] * object2.matrix[k][j]
            return result
        else:
            print("Matrices aren't the proper sizes.")
            return 1

    def __getitem__(self, key):
        return self.matrix[key[0]][key[1]]

    def __str__(self):
        number_of_rows = Matrix.size(self)[0]
        matrix_string = ''

        for i in range(number_of_rows):
            matrix_string += ('|' + ' '.join(map(lambda x: '{0:8.1f}'.format(x), self.matrix[i])) + '|\n')
        return matrix_string

    def __len__(self):
        return len(self.matrix)

    def size(self):
        number_of_rows = len(self)
        number_of_columns = len(self.matrix[0][:])

        return number_of_rows, number_of_columns
