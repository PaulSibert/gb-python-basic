# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.sum

input_sum = 0
do = True
while do:
    input_str = input()
    input_list = input_str.split()
    for input_element in input_list:
        if input_element.lower() == "exit":
            do = False
            break
        elif input_element.isdigit():
            input_sum += int(input_element)
        else:
            pass
    print(input_sum)
