# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

mon_in_year = 12
mon_in_season = 3
seasons_dict = {0:"зима", 1:"Весна", 2:"лето", 3:"осень"}
seasons_list = ["зима", "весна", "лето", "осень"]

mon_str = ""
while not mon_str.isdigit():
    mon_str = input("Введите номер месяца: ")
mon = int(mon_str)
mon = mon if mon < mon_in_year else mon % mon_in_year
mon //= mon_in_season
print(seasons_list[mon])
print(seasons_dict.get(mon))
