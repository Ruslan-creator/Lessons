'''
Реализуйте базовый класс Car .
● у класса должны быть следующие атрибуты: speed, color, name, is_police ( булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar , SportCar , WorkCar , PoliceCar ;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 ( TownCar) и 40 ( WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Вызовите методы и покажите результат.
'''


class Car:
    is_police = False

    def __init__(self, name, speed, color, ispolice=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = ispolice

    def go(self):
        return 'The car is go'

    def stop(self):
        return 'The car is stop'

    def turn_direction(self, direction):
        return 'The car is turn ' + direction

    def show_speed(self, speed):
        return self.speed


class TownCar(Car):
    def show_speed(self, speed):
        if speed >= 60:
            return 'The current speed is to high'
        else:
            return 'The current speed of the car ' + str(speed)


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self, speed):
        if speed >= 40:
            return 'The current speed is to high'
        else:
            return 'The current speed of the car ' + str(speed)


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


Ford = SportCar('Ford', 140, 'red')
print(Ford.name, Ford.speed, Ford.color, Ford.is_police)
print(Ford.go(), Ford.turn_direction('Village'), Ford.stop())

Mazda = TownCar('Mazda', 50, 'green')
print(Mazda.name, Mazda.speed, Mazda.color, Mazda.is_police)
print(f'{Mazda.go()}, {Mazda.turn_direction("Lake")}, {Mazda.stop()}, {Mazda.show_speed(Mazda.speed)}')

BMW = WorkCar('BMW', 41, 'white')
print(BMW.name, BMW.speed, BMW.color, BMW.is_police)
print(f'{BMW.go()}, {BMW.turn_direction("River")}, {BMW.stop()}, {BMW.show_speed(BMW.speed)}')

Ferrari = PoliceCar('Ferrari', 220, 'blue')
print(Ferrari.name, Ferrari.speed, Ferrari.color, Ferrari.is_police)
print(Ferrari.go(), Ferrari.turn_direction('City'), Ferrari.stop())
