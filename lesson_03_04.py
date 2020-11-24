# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def float_input(promt = ""):
    """Функция ввода с приведением к типу float
        При вводе значения, приведение которого к типу float невозможно, возвращает None
    Аргументы:
        promt - str - подсказка ввода, необязательный
    """
    result = None
    try:
        result = float(input(promt))
    except ValueError:
        pass
    return result


def int_input(promt = ""):
    """Функция ввода с приведением к типу int
        При вводе значения, приведение которого к типу int невозможно, возвращает None
    Аргументы:
        promt - str - подсказка ввода, необязательный
    """
    result = None
    try:
        result = int(input(promt))
    except ValueError:
        pass
    return result

def slow_power(base, power):
    """
    Возведение в степень с помощью оператора **
    :param base: float - основание
    :param power: int - степень
    :return:
    """
    return base ** power


def slow_power_loop(base, power):
    """
    Возведение в степень с помощью цикла
    :param base: float - основание
    :param power: int - степень
    :return:
    """
    step = -1 if power < 0 else 1
    result = 1.0
    for index in range(0, power, step):
        result = result * base if step >= 0 else result / base
    return result


input_base = None
while input_base is None:
    input_base = float_input("Введите основание: ")

input_power = None
while input_power is None:
    input_power = int_input("Введите степень: ")

print(slow_power(input_base, input_power))
print(slow_power_loop(input_base, input_power))
