# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
# — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.

max_row_count = 10
row_count_str = ""
goods = list()
row_dict_template = {"Название":"", "Цена":0, "Количество":0, "Ед":""}
while not row_count_str.isdigit():
    row_count_str = input("Введите количество строк товаров: ")
row_count = int(row_count_str)

if row_count > max_row_count:
    print("Количество строк товаров ({}) превышает максимльное ({}), установлено количество строк {}".format(row_count, max_row_count, max_row_count))
    row_count = max_row_count

index = 0
while index < row_count:
    index += 1
    print("Строка {:>2}".format(index))
    row_dict = row_dict_template.copy()
    for spec in row_dict.items():
        row_dict.update({spec[0]:input("    {}: ".format(spec[0]))})
    goods.append((index, row_dict.copy()))

print(goods)

stats = row_dict_template.copy()
for spec in stats.items():
    stat_list = list()
    for goods_row in goods:
       stat_list.append(goods_row[1].get(spec[0]))
    stats.update({spec[0]: list(set(stat_list))})

print(stats)
