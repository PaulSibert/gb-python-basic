# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def slow_capitalize(input_str):
    """
    Функция делает прописной первую букву в строке, остальные делает строчными
    :param input_str: входящая строка
    :return: str: результат обработки строки
    """
    return input_str.capitalize()


input_str = input()
print(slow_capitalize(input_str))
# Вариант 1
input_list = []
for input_element in input_str.split():
    input_list.append(slow_capitalize(input_element))
print(" ".join(input_list))
# Вариант 2
print(input_str.title())
