# range тип, представляющий целочисленный диапозон
one_to_hundred: range = range(1, 101)  # можно указывать верхнюю и нижнюю границу
print(one_to_hundred)
one_to_nine: range = range(10)  # можно указать только верхнюю границу если нижняя равна 0(по умолчанию равна 0)
print(one_to_nine)
one_to_hundred_evens: range = range(0, 101, 2)
print(one_to_hundred_evens)


print(list(one_to_hundred_evens))

from_100_to_0: range = range(100, -1, -1)
print(list(from_100_to_0))
