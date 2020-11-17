# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
multiplier = 1.10

current_dist_str = ""
while not current_dist_str.isdigit():
    current_dist_str = input("Введите текущий результат: ")
current_dist = int(current_dist_str)

target_dist_str = ""
while not target_dist_str.isdigit():
    target_dist_str = input("Введите целевой результат: ")
target_dist = int(target_dist_str)

target_day = 0

while current_dist < target_dist:
    current_dist = current_dist * multiplier
    target_day += 1

print("Достижение цели через {} дней".format(target_day))
