# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("input_log.txt", "w") as log_file:
    input_str = input()
    while len(input_str) > 0:
        log_file.write(input_str + "\n")
        input_str = input()
