'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def method(cls, day_month_year):
        my_calendar = day_month_year.split('-')
        return int(my_calendar[0]), int(my_calendar[1]), int(my_calendar[2])

    @staticmethod
    def proverka(day, month, year):
        if day < 0 or day > 31:
            return 'Incorrect day'
        elif month < 1 or month > 12:
            return 'Incorrect month'
        elif year < 1 or year > 2021:
            return ' Incorrect year'
        else:
            return 'Everything all right'

    def __str__(self):
        print(f'Correct data is {Data.method(day_month_year)}')


print(*Data.method('8-12-2021'))
print(Data.proverka(8, 12, 2021))
