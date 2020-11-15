class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result_list = []
        for i, _ in enumerate(self.matrix):
            for col in self.matrix[i]:
                result_list.append(f'{col} ')
            result_list.append('\n')
        result_str = ''
        return result_str.join(result_list)

    def __add__(self, other):

        # Здесь делаем проверку размеров матриц
        identical = ValueError('Матрицы разного размера')
        if len(self.matrix) != len(other.matrix):
            raise identical
        for i, _ in enumerate(self.matrix):
            if len(self.matrix[i]) != len(other.matrix[i]):
                raise identical

        # Здесь выполняем сложение матриц
        result = []
        for i, _ in enumerate(self.matrix):
            line = []
            for j, _ in enumerate(self.matrix[i]):
                sum_m = self.matrix[i][j] + other.matrix[i][j]
                line.append(sum_m)
            result.append(line)
        return Matrix(result)


# Проверяем сложение матриц разных размеров
m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_3 = Matrix([[1, 2], [4, 5], [7, 8]])
try:
    m_4 = m_1 + m_2 + m_3
    print(m_4)
except ValueError as e:
    print(f'Ошибка слагаемых - {e}')

# Проверяем сложение матриц одинаковых размеров
m_5 = Matrix([[1, 2, 3, 44], [4, 5, 6, 43], [7, 8, 9, 7]])
m_6 = Matrix([[1, 2, 3, 22], [4, 5, 6, 1], [7, 8, 9, 15]])
m_7 = Matrix([[1, 2, 33, 0], [4, 5, 14, 21], [7, 8, 93, 4]])
m_8 = Matrix([[23, 4, 22, 45], [12, 43, 2, 16], [32, 23, 4, 14]])
try:
    m_9 = m_5 + m_6 + m_7 + m_8
    print(m_9)
except ValueError as e:
    print(f'Ошибка слагаемых - {e}')
