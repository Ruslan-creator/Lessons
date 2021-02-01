'''
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
её на экран.
'''


with open('numbers.txt', 'w', encoding='UTF-8') as file:
    numbers = input('Enter your numbers with space: ')
    file.write(numbers)

with open('numbers.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    print(sum([int(number) for number in content.split()]))