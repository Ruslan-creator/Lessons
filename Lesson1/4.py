number = int(input('Enter your number: '))
print(max(str(number)))

number = int(input('Enter your number: '))
max = number % 10
number= number//10
while number > 0:
    if number % 10 > max:
        max = number%10
        number = number//10
print(max)
