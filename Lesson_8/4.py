'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
'''


class Sklad:
    def __init__(self, name):
        self.name = name


class Orgtecnika:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(Orgtecnika):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color


class Xerox(Orgtecnika):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight


class Skaner(Orgtecnika):
    def __init__(self, name, price, shape):
        super().__init__(name, price)
        self.shape = shape
