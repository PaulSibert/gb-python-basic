# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def read_float(input_str, error_message):
    result = None
    error = False
    try:
        result = float(input_str)
    except ValueError:
        error = True
        print(error_message)
    return result, error


script_name, working_hours_par, rate_par, bonus_par = argv

read_errors = False

working_hours, read_error = read_float(working_hours_par, "Неверный параметр 1")
read_errors = read_errors or read_error
rate, read_error = read_float(rate_par, "Неверный параметр 2")
read_errors = read_errors or read_error
bonus, read_error = read_float(bonus_par, "Неверный параметр 3")
read_errors = read_errors or read_error

if not read_errors:
    print("Зарплата: {:.2f}".format((working_hours * rate) + bonus))
