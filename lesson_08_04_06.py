# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Store:
    goods = []
    goods_in_office = {}
    goods_info = []
    goods_in_office_info = {}

    @classmethod
    def add(cls, goods_item):
        cls.goods.append(goods_item)
        cls.goods_info = [{"barcode": el.barcode, "description": str(el)} for el in cls.goods]
        for el in cls.goods_info:
            el_copy = el.copy()
            el_copy.update({"qty": cls.goods_info.count(el)})
            while cls.goods_info.count(el) > 0:
                cls.goods_info.remove(el)
            cls.goods_info.append(el_copy)

    @classmethod
    def out(cls, goods_item, office):
        if cls.goods.count(goods_item) == 0:
            print("Не хватает техники ({}) на складе".format(goods_item))
        else:
            cls.goods.remove(goods_item)
            cls.goods_info = [{"barcode": el.barcode, "description": str(el), "qty": 1} for el in cls.goods]
            for el in cls.goods_info:
                el_copy = el.copy()
                el_copy.update({"qty": cls.goods_info.count(el)})
                while cls.goods_info.count(el) > 0:
                    cls.goods_info.remove(el)
                cls.goods_info.append(el_copy)
            if cls.goods_in_office.get(office) is None:
                cls.goods_in_office.update({office:[]})
            cls.goods_in_office.get(office).append(goods_item)

            if cls.goods_in_office_info.get(office) is None:
                cls.goods_in_office_info.update({office:[]})

            office_info = [{"barcode": el.barcode, "description": str(el)} for el in cls.goods_in_office.get(office)]
            for el in office_info:
                el_copy = el.copy()
                el_copy.update({"qty": office_info.count(el)})
                while office_info.count(el) > 0:
                    office_info.remove(el)
                office_info.append(el_copy)
            cls.goods_in_office_info.update({office: office_info})


class Goods:

    def __init__(self, name, model, barcode):
        self.name = name
        self.model = model
        self.barcode = barcode

    def __str__(self):
        return "{} ({}) - {}".format(self.name, self.model, self.barcode)

    def __eq__(self, other):
        return self.barcode == other.barcode



class Printer(Goods):

    def __init__(self, name, model, barcode, print_type):
        super().__init__(name, model, barcode)
        self.print_type = print_type

    def __str__(self):
        return "{} {} ({}) - {}".format(self.name,  self. print_type, self.model, self.barcode)


class Scanner(Goods):

    def __init__(self, name, model, barcode, dpi):
        super().__init__(name, model, barcode)
        self.dpi = dpi

    def __str__(self):
        return "{} {} ({}) - {}".format(self.name, self.dpi, self.model, self.barcode)


class CopyMachine(Goods):

    def __init__(self, name, model, barcode, speed):
        super().__init__(name, model, barcode)
        self.speed = speed

    def __str__(self):
        return "{} {} ({}) - {}".format(self.name, self.speed, self.model, self.barcode)


printer_1 = Printer("Принтер лазерный", "HP-101", "12345", "Лазер ЧБ")
Store.add(printer_1)
Store.add(Printer("Принтер лазерный", "HP-101", "12345", "Лазер ЧБ"))
print(Store.goods_info)
Store.out(printer_1, "central")
print(Store.goods_info)
print(Store.goods_in_office_info)
