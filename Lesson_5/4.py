'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
'''

translate = {' One':' Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
with open(r'Lesson_2_4.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    new_content = [f'{translate[line.split(" — ")[0]]} - {line.split(" — ")[-1]}' for line in content]
    print(*new_content)

with open(r'Lesson_2_4_1.txt', 'w', encoding='UTF-8') as files:
    files.writelines(new_content)