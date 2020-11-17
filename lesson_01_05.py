# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
proceeds = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))
profit = proceeds - costs
if profit >= 0:
    print("Фирма работает с прибылью: {}".format(abs(profit)))
    if proceeds != 0:
        profitability = profit / proceeds
    else:
        profitability = 0
    print("Рентабельность: {}".format(profitability))
else:
    print("Фирма работает с убытком: {}".format(abs(profit)))

employees = int(input("Введите количество сотрудников: "))
if employees != 0:
    profit_per_employee = profit / employees
else:
    profit_per_employee = profit

if profit_per_employee >= 0:
    print("Прибыль на сотрудника: {}".format(abs(profit_per_employee)))
else:
    print("Убыток на сотрудника: {}".format(abs(profit_per_employee)))
