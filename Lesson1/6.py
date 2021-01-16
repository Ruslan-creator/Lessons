a = int(input('How much km did you run in first day? : '))
b = int(input('Enter your goal in km: '))
day = 1
while a < b:
    a = a + 0.1 * a
    day += 1
    print(f'On {day} day: {round(a,2)}')

print(f'Your goal will be achieved on {day} day')