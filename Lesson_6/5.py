'''
Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title ( название) и метод draw ( отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
'''


class Stationery:
    atribut_title = 'title'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки класса Pen')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки класса Pencil')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки класса Handle')


my_pen = Pen()
my_pen.draw()
my_pencil = Pencil()
my_pencil.draw()
my_handle = Handle()
my_handle.draw()
