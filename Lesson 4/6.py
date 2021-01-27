"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

start = int(input('Enter your number for start generation: '))
end = int(input('Enter your number for stop generation: '))
counter = count(start)

for el in range(start, end + 1):
    print(next(counter))

cycler = cycle([1, 2, 3])
action = None
print('Enter q for stop process: ')

while action != 'q':
    print(next(cycler), end='')
    action = input()
