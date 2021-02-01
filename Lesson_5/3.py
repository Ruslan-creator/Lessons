'''
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''


with open(r'C:\Users\Руслан\Desktop\Lesson_2_3.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    person_with_low_salary = []
    average_salary = 0
    for el in content:
        surname, salary = el.split()
        salary = float(salary)
        average_salary += salary
        if salary < 20000:
            person_with_low_salary.append(surname)

# нагуглил её, ибо не понимал,как список в f строке привести к строке
print(f'Salary less 20000 for: {", ".join(str(x) for x in person_with_low_salary)}')
print(f'Average salary are: {round(average_salary/len(content))}')
