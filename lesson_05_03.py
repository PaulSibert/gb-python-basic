# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("input_log.txt", "r") as log_file:
    file_content = log_file.readlines()

employees = [{"name":st.split()[0], "salary":int(st.split()[1])} for st in file_content if len(st.split()) == 2 and st.split()[1].isdigit()]
employees_out = [emp.copy() for emp in employees if emp["salary"] < 20000]
print(employees_out)

salary_data = [el["salary"] for el in employees_out]
print("Средняя ЗП: {:.2f}".format(sum(salary_data)/len(salary_data)))
