# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

type_examples = [True, 13, 3.14, "Мама мыла раму", [1, 2, 3, 4, 5]]
print("Type examples:")
for type_example in type_examples:
    print("{} : {}".format(type_example, type(type_example)))