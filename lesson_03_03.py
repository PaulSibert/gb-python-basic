# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

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


def max_two_of_three(arg_one, arg_two, arg_three):
    """
    Функция возвращает сумму 2 максимальных из 3 аргументов
    :param arg_one: int: первый аргумент
    :param arg_two: int: второй аргумент
    :param arg_three: int: третий аргумент
    :return: int: сумма 2 максимальных из 3 аргументов
    """
    return arg_one + arg_two + arg_three - min(arg_one, arg_two, arg_three)

input_arg_one = None
while input_arg_one is None:
    input_arg_one = int_input("Введите первый аргумент: ")

input_arg_two = None
while input_arg_two is None:
    input_arg_two = int_input("Введите второй аргумент: ")

input_arg_three = None
while input_arg_three is None:
    input_arg_three = int_input("Введите третий аргумент: ")

print("Результат: {}".format(max_two_of_three(input_arg_one, input_arg_two, input_arg_three)))
