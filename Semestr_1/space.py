import numbers


class Matrix:
    '''Работа с матрицами(квадртными)'''
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        """Сложение матриц """
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)

    def __mul__(self, other):
        """ Умножение матрицы на матрицу и матрицы на число """
        length = len(self.my_list)
        result_matrix = [[0 for i in range(length)] for i in range(length)]

        if isinstance(other.my_list, numbers.Number):
            result_matrix = [list(map(lambda x: x * other.my_list, z)) for z in self.my_list]
        else:
            for i in range(length):
                for j in range(length):
                    for k in range(length):
                        result_matrix[i][j] += self.my_list[i][k] * other.my_list[k][j]
        self.my_list = result_matrix
        return Matrix.__str__(self)

    def __eq__(self, other):
        '''Проверка на равенство матриц'''
        return self.my_list == other.my_list



A = Matrix([[1, 2, 3], [1, 0, -1], [1, 1, 1]])
B = Matrix([[3, 4, 5], [6, 0, -2], [7, 1, 8]])
print(A + B)
print(A * B)
C = Matrix(2)
print(A * C)
print(A == B)
