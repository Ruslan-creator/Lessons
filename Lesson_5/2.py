'''
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
'''
with open(r'Lesson_2.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    for lineNumber, line in enumerate(content, start=1):
        length = len(line.split())
        print(lineNumber, length)
