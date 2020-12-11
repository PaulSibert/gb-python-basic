# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open("input_log.txt", "r") as log_file:
    file_content = log_file.readlines()

fin_data = [{"firm":st.split()[0], "firm_type":st.split()[1], "proceeds":int(st.split()[2]), "costs":int(st.split()[3])} for st in file_content]
output_fin_data = [{el["firm"]: el["proceeds"] - el["costs"]} for el in fin_data]
avg_profit_data = [el["proceeds"] - el["costs"] for el in fin_data if el["proceeds"] - el["costs"] > 0]
output_fin_data.append({"avg_profit": sum(avg_profit_data)/len(avg_profit_data)})

with open("output_log.json", "w") as log_file:
    json.dump(output_fin_data, log_file)
