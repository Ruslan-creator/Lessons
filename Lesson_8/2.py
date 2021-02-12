'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        inp_data = input('Enter your number: ')
        inp_data_2 = input('Enter your number: ')
        if inp_data == 'f' or inp_data_2 == 'f':
            break
        inp_data = int(inp_data)
        inp_data_2 = int(inp_data_2)

        if inp_data < 0 or inp_data_2 < 0:
            raise MyError('You entered a negative number')
        elif inp_data_2 == 0:
            raise MyError('Split on 0 is forbidden')
    except MyError:
        print('You entered not a number')
