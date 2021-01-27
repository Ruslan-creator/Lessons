def get_max_two_digits(a, b, c):
    list = [a, b, c]
    list.sort(reverse=True)
    sum = list[0] + list[1]
    return sum


result = get_max_two_digits(1, 14, 2)
print(f'Сумма наибольших двух аргументов равна: {result}')
