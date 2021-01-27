number = int(input('Enter your numbers from 1 till 12: '))
months = {
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumm': [9, 10, 11]
}
for k, v in months.items():
    if number in v:
        print(k)

months_list = ['Winter', 'Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumm',
               'Autumm',
               'Autumm']
number = int(input('Enter your numbers from 1 till 12: '))
print(months_list[number - 1])
