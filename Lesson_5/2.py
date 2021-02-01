'''
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
'''
with open(r'C:\Users\Руслан\Desktop\Lesson_2.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    for line, stroka in enumerate(content, start=1):
        el = len(stroka.split())
        print(line, el)
