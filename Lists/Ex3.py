# нужно создать список случайных целых чисел заданой длины.
# вывести его сумму, среднеарефм и геометрическое
from random import randint


def create_random_numbers(lenght: int, a: int, b: int) -> list[int]:
    numbers: list[int] = []
    i = 0
    while i < lenght:
        random_number: int = randint(a, b)
        numbers.append(random_number)
        i += 1
    return numbers


lenght: int = int(input("Введите количество чисел: "))
frirst: int = int(input("Введите нижнюю границу: "))
second: int = int(input("Введите верхнюю границу: "))

random_numbers: list[int] = create_random_numbers(lenght, frirst, second)

print(random_numbers)
