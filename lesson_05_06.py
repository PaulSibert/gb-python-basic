# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("input_log.txt", "r") as log_file:
    file_content = log_file.readlines()

edu_data = [{st.split()[0].replace(":", ""): [el for el in st.split()]} for st in file_content]

for edu_el in edu_data:
    for edu_key in edu_el.keys():
        new_value = 0
        input_list = edu_el.get(edu_key)
        for input_value in input_list:
            temp_str = input_value.lower()
            temp_str = input_value.replace("-", "")
            temp_str = input_value.replace(".", "")
            temp_str = temp_str.removesuffix("(л)").removesuffix("(лаб)").removesuffix("(пр)")
            temp_str = temp_str.strip()
            new_value = new_value + int(temp_str) if temp_str.isdigit() else new_value
        edu_el.update({edu_key: new_value})

print(edu_data)
