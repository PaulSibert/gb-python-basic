# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
multiplier = 3
number_str = ""
while not number_str.isdigit():
    number_str = input("Введите число: ")
number = int(number_str)

numbers = []
numbers.append(number)
while len(numbers) < multiplier:
    prev_number = numbers[len(numbers) - 1]
    current_number = int("{}{}".format(prev_number, abs(number)))
    numbers.append(current_number)
number_total = 0

for current_number in numbers:
    number_total += current_number
print(number_total)
