# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class ExceptionInvalidDate(Exception):
    pass

class Date:

    def __init__(self, date_str: str):
        self.day, self.mounth, self.year = Date.date(date_str)

    def __str__(self):
        return "{}-{}-{}".format(self.day, self.mounth, self.year)

    @classmethod
    def date(cls, date_str):
        date_list = date_str.split("-")
        day = int(date_list[0])
        mounth = int(date_list[1])
        year = int(date_list[2])
        Date.check_date(day, mounth, year)
        return day, mounth, year

    @staticmethod
    def check_date(day, mounth, year):
        long_mounths = [1, 3, 5, 7, 8, 10, 12]
        if mounth < 1 or mounth > 12:
            raise ExceptionInvalidDate
        if day < 1 or day > 31:
            raise ExceptionInvalidDate
        if long_mounths.count(mounth) == 0 and day > 30:
            raise ExceptionInvalidDate
        elif mounth == 2:
            if year % 4 == 0 and day > 29:
                raise ExceptionInvalidDate
            elif year % 4 != 0 and day > 28:
                raise ExceptionInvalidDate
        elif day > 30:
            raise ExceptionInvalidDate


print(Date.date("1-12-2020"))
wedding_date = Date("26-07-2014")
print(wedding_date)
wrong_date = Date("32-13-2020")
