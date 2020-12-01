# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numerals = dict(one="один", two="два", three="три", four="четыре", five="пять", six="шесть", seven="семь",
                eight="восемь", nine="девять", zero="ноль")

with open("input_log.txt", "r") as log_file:
    file_content = log_file.readlines()

with open("output_log.txt", "w") as log_file:
    log_file.writelines([" ".join([word if numerals.get(word.lower()) is None else numerals.get(word.lower()) for word in st.split()]) + "\n" for st in file_content])
