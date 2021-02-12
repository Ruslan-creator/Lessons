'''
Реализовать базовый класс Worker (работник).
● определить атрибуты: name , surname , position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker ;
● в классе Position реализовать методы получения полного имени сотрудника
( get_full_name ) и дохода с учётом премии ( get_total_income );
● проверить работу примера на реальных данных: создать экземпляры класса PoЫsition,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


Ы
hr = Position('Ivan', ' Smirnov', 'HR', {"wage": 600, "bonus": 160})

print(hr.get_full_name(), hr.get_total_income())
