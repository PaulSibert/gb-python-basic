# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("input_log.txt", "r") as log_file:
    file_content = log_file.readlines()
file_info = {"strings_count":len(file_content), "strings":[{"words":len(st.split())} for st in file_content]}
print(file_info)
