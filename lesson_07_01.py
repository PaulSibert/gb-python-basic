# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, elements: list):
        self.elements = [[el for el in row] for row in elements]

    def __str__(self):
        result = ""
        border = "|"
        for row in self.elements:
            result += border
            for el in row:
                result += "{:>4}".format(el)
            result += border
            result += "\n"
        return result

    def __add__(self, other):
        result = [[el for el in row] for row in self.elements]
        for row in range(len(result)):
            for col in range(len(result[row])):
                result[col][row] += other.elements[col][row]
        return Matrix(result)


m_alpha = Matrix([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
m_beta = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(m_alpha)
print(m_beta)
print(m_alpha + m_beta)
