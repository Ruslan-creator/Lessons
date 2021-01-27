def division(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        return
    return c


g_1 = float(input('Enter your numbers: '))
g_2 = float(input('Enter your numbers: '))

print(division(g_1, g_2))
