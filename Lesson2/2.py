numbers = input('Enter your numbers: ').split()
for el in range(0, len(numbers) - 1, 2):
    numbers[el], numbers[el + 1] = numbers[el + 1], numbers[el]
print(numbers)
# не знаю как вывести исходный список(
