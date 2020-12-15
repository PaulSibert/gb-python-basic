# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNum:

    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNum(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.imaginary * other.imaginary, self.imaginary * other.real + self.real * other.imaginary)

    def __str__(self):
        return "{} + {}i".format(self.real, self.imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary


alpha = ComplexNum(10, 2)
print(alpha)
beta = ComplexNum(-22, 1)
print(beta)
print(alpha + beta)
print(beta * alpha)
