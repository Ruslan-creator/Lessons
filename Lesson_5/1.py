'''
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
'''


with open('text.txt', 'w', encoding='UTF-8') as file:
    while True:
        text = input('Enter your sentence: ')
        if text == ' ':
            break
        file.write(f'{text}\n')