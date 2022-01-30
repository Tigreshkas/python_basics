# Реализовать класс Matrix (матрица).
class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in row) for row in self.array)  # вывод матрицы в виде матрицы

    def __add__(self, other):
        sum_array = []
        for row in range(len(self.array)):
            sum_array.append([])
            for num in range(len(self.array[row])):
                sum_array[row].append(int(self.array[row][num]) + int(other.array[row][num]))  # добавляем в список
                # сумму чисел складываемых матриц
        return Matrix(sum_array)


matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix([[1, 3], [2, 4]])
print(matrix_1)
print('------------')
print(matrix_2)
print('------------')
print(matrix_1 + matrix_2)
