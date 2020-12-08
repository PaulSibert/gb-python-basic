# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from random import randint

class Clothes(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def value(self):
        pass

    @property
    def description(self):
        return self.name


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def value(self):
        return self.size * 2.0 + 0.3

    @property
    def description(self):
        return "{} размер {}".format(self.name, self.size)


class Suit(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def value(self):
        return self.height / 6.5 + 0.5

    @property
    def description(self):
        return "{} размер {}".format(self.name, self.height)


clothes_to_produce = [Coat("Пальто арт.{}".format(el), randint(40, 50)) if randint(1, 2) > 1 else Coat("Костюм арт.{}".format(el), randint(160, 200)) for el in range(randint(5, 10))]
total_value = 0.0
for clothes in clothes_to_produce:
    current_value = clothes.value()
    print("{} ({}) - {:.2f}".format(clothes, clothes.description, current_value))
    total_value += current_value
print("Итого: {:.2f}".format(total_value))
