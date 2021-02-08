"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер ( для пальто) и рост ( для костюма) . Это могут быть обычные числа: V и
H , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property .
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def square(self):
        pass

    @staticmethod
    def full_square(clothes):
        summa = 0
        for el in clothes:
            summa += el.square()
        return summa


class Coat(Clothes):
    def __init__(self, size,name):
        super().__init__(name)
        self.__size = size

    def square(self):
        return self.__size/6.5 + 0.5

    def __str__(self):
        return f'Square of Coat = {round(self.square())}'


class Suit(Clothes):
    def __init__(self,hight, name):
        super().__init__(name)
        self.__hight = hight

    def square(self):
        return 2*self.__hight + 0.3

    def __str__(self):
        return f'Square of Suit = {round(self.square())}'


coat = Coat(2, 'Coat')
suit = Suit(4, 'Suit')
print(coat)
print(suit)
print(f'Total square = {round(Clothes.full_square([coat,suit]))}')
