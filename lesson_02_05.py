# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

ratings = [100, 98, 95, 80, 50, 10, 10]
ratings.sort(reverse=True)
print("Текущий рейтинг")
print(ratings)

rating_str = ""
while not rating_str.isdigit():
    rating_str = input("Введите новый результат: ")
rating = int(rating_str)

ratings.append(rating)
ratings.sort(reverse=True)

print("Новый рейтинг")
print(ratings)
