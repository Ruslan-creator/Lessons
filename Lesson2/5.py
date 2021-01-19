my_list = [7, 5, 3, 3, 2]
while True:
    number = int(input('Enter your whole number: '))
    for i in range(1, len(my_list)):
        if number >= max(my_list):
            my_list.insert(0, number)
            break
        elif number <= min(my_list):
            my_list.append(number)
            break
        elif my_list[i - 1] >= number >= my_list[i]:
            my_list.insert(i, number)
            break
    print(my_list)
-------------------------------------------------------------------------
my_list = [7, 5, 3, 3, 2]
number = int(input('Enter your whole number: '))
while True:
    my_list.append(number)
    my_list.sort(reverse=True)
    print(my_list)
    number = int(input('Enter your whole number: '))