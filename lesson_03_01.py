# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

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


def safe_div(dividend, divisor):
    """Функция безопасного деления
        При делении на 0 выводит соответствующее сообщение и возвращает None
    Аргументы:
        dividend - float - делимое, обязательный
        divisor - float- делитель, обязательный
    Пример вызова
        dividend = 10
        divisor = 2
        result = safe_div(dividend, divisor)
    """
    result = None
    if divisor == 0:
        print("Деление на 0")
    else:
        result = dividend / divisor
    return result


input_dividend = None
while input_dividend is None:
    input_dividend = float_input("Введите делимое: ")

input_divisor = None
while input_divisor is None:
    input_divisor = float_input("Введите делитель: ")

input_result = safe_div(input_dividend, input_divisor)
if input_result is not None:
    print("{} / {} = {}".format(input_dividend, input_divisor, input_result))
