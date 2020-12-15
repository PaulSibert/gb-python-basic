# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.

class Road:

    _height = 0.05
    _weight = 2500

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        return self.length * self.width * Road._height * Road._weight


highway = Road(10000, 40)
print(highway.mass())