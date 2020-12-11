# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ExceptionMyDivisionByZero(Exception):

    def __init__(self, txt):
        self.txt = txt


def my_division(dividend, divider):
    if divider == 0:
        raise ExceptionMyDivisionByZero("деление на ноль")
    else:
        return dividend / divider


try:
    print(my_division(1000, 125))
    print(my_division(1000, 0))
except ExceptionMyDivisionByZero as msg:
    print(msg)
