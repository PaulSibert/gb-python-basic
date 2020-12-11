# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

max_list_size = 13
xchg_list = []
list_size_str = ""
while not list_size_str.isdigit():
    list_size_str = input("Введите размер списка: ")
list_size = int(list_size_str)

if list_size > max_list_size:
    print("Размер списка ({}) превышает максимальный ({}), установлен размер {}".format(list_size, max_list_size, max_list_size))
    list_size = max_list_size

index = 0
while index < list_size:
    index += 1
    xchg_list.append(input("Введите элемент {:>3}:".format(index)))

index = 1
while index < list_size:
    if index % 2 > 0:
        xchg_list.insert(index - 1, xchg_list.pop(index))
    index += 1

print("Список после обработки:")
for el in xchg_list:
    print(el)
