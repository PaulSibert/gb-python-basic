# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.direction = ""
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print("{} {} поехал".format(self.color, self.name))

    def stop(self):
        self.speed = 0
        print("{} {} остановился".format(self.color, self.name))

    def turn(self, direction):
        self.direction = direction
        print("{} {} повернул на {}".format(self.color, self.name, self.direction))

    def show_speed(self):
        if self.speed > 0:
            print("{} {} едет со скоростью {} км/ч".format(self.color, self.name, self.speed))
        else:
            print("{} {} стоит на месте".format(self.color, self.name))


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("{} {} превышает скорость".format(self.color, self.name))


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("{} {} превышает скорость".format(self.color, self.name))


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True


police_car_1 = PoliceCar("Полицейский форд г.н. 001аа", "Cиний")
police_car_1.go(100)
police_car_1.show_speed()
police_car_1.turn("север")
police_car_1.stop()
police_car_1.show_speed()

police_car_1 = TownCar("Вольво г.н. 006хх", "Серебристый")
police_car_1.go(70)
police_car_1.show_speed()
police_car_1.turn("юг")
police_car_1.stop()
police_car_1.show_speed()

police_car_1 = WorkCar("Камаз г.н. 007аа", "Оранжевый")
police_car_1.go(50)
police_car_1.show_speed()
police_car_1.turn("запад")
police_car_1.stop()
police_car_1.show_speed()

police_car_1 = SportCar("Шевроле г.н. 666хх", "желтый")
police_car_1.go(140)
police_car_1.show_speed()
police_car_1.turn("восток")
police_car_1.stop()
police_car_1.show_speed()
