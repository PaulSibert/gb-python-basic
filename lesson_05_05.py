# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint
from functools import reduce

strings_count = randint(1, 10)
words_count = randint(1, 10)
with open("input_log.txt", "w") as log_file:
    log_file.writelines([" ".join([str(randint(1, 100)) for wrd in range(words_count)]) + "\n" for st in range(strings_count)])

with open("input_log.txt", "r") as log_file:
    file_content = log_file.readlines()

numeric_data = [int(el) for st in file_content for el in st.split() if el.isdigit()]

print(numeric_data)
print(reduce(lambda a, b: a + b, numeric_data))
