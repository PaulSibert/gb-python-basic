# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    incomes = {"junior": {"wage": 50000, "bonus": 10000}, "middle": {"wage": 100000, "bonus": 30000}}

    def __init__(self, name, surname, income):
        self.name = name
        self.surname = surname
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return "{} {}".format(self.name, self.surname)

    def get_total_income(self):
        income_info = Worker.incomes.get(self._income)
        if income_info is not None:
            result = income_info.get("wage") + income_info.get("bonus")
        else:
            result = None
        return result


junior_1 = Position("Иванов", "Иван", "junior")
middle_1 = Position("Горбунков", "Семен", "middle")


print(junior_1.get_full_name())
print(junior_1.get_total_income())
print(middle_1.get_full_name())
print(middle_1.get_total_income())
