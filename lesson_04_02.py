# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

input_str = input("Введите список: ")
input_list = [int(el) for el in input_str.split() if el.isdigit()]
result = [input_list[index] for index in range(1, len(input_list)) if input_list[index] > input_list[index - 1]]
print(result)
