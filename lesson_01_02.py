# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
seconds_str = ""
while not seconds_str.isdigit():
    seconds_str = input("Введите время в секундах: ")
seconds_total = int(seconds_str)
seconds = seconds_total
minutes = seconds // 60
seconds %= 60
hours = minutes // 60
minutes %= 60
print("{} секунд это {:02}:{:02}:{:02}".format(seconds_total, hours, minutes, seconds))
