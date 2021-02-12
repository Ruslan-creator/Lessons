'''
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
'''
class Sklad:
    storage = {}

    def accept(self, department, count: int, technic):
        if self.storage.get(department) is None:
            self.storage[department] = {technic: 0}
        elif self.storage[department].get(technic) is None:
            self.storage[department][technic] = 0
        self.storage[department][technic] += count


class Technik:
    def __init__(self, color, price, model):
        self.color = color
        self.price = price
        self.model = model


class Printer(Technik):
    def __init__(self, laser, color, price, model):
        Technik.__init__(self, color, price, model)
        self.laser = laser


class Scaner(Technik):
    def __init__(self, max_weight, color, price, model):
        super().__init__(color, price, model)
        self.max_weight = max_weight


class Xerox(Technik):
    def __init__(self, volume, color, price, model):
        super().__init__(color, price, model)
        self.volume = volume


m = Sklad()
m.accept('IT', 1, 'scanner')
m.accept('IT', 2, 'printer')
m.accept('Marketing', 3, 'printer')
m.accept('Marketing', 4, 'printer')
print(*m.storage.items())
