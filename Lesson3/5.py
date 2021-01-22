while True:
    numbers = input('Enter your number: ').split()
    sum = 0
    exit = False
    for el in numbers:
        if el == '$':
            print('Sorry')
            exit = True
            break
        sum += int(el)
    print(sum)
    if exit == True:
        break
