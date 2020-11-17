# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number_str = ""
while not number_str.isdigit():
    number_str = input("Введите число: ")
number = int(number_str)
max_digit = 0;
while number > 0:
    current_digit = number % 10
    if max_digit < current_digit:
        max_digit = current_digit
    number//= 10
print("Наибольшая цифра: {}".format(max_digit))
