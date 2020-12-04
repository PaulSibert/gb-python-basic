# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep


class TrafficLight:
    _timings = {"Red":7, "Yellow": 2, "Green": 7}

    def __init__(self):
        self.__color = ""

    def running(self):
        print("on")
        for timing in TrafficLight._timings.keys():
            self.__color = timing
            print(self.__color)
            sleep(TrafficLight._timings.get(timing))
        print("off")

tl = TrafficLight()
tl.running()
