# Типы данных которые хранят в себе еденичное значиение, обычно называется скаляры (int, float, bool)
# Типы которые могут хранить в себе множество значений, обычно называется коллекциями
# STR- коллекция символов или подстрок
# list- коллекция пронумерованных элементов опредеенного типа
from  math import sqrt, log2, factorial
numbers: list[int] = [1, 12]
print(numbers)

# В список по ходу программы можно добавлять или удалять эдементы

# Два способа создания пустого списка
empty_list_1: list[int] = []
empty_list_2: list[int] = list()

# Заполнение списка вручную
names: list[str] = []
print(names)
# функции которые ассациированы(связаны) с КОНКРЕТНЫМ обьектом, называются методы, для их вызова
# нужно после обьекта поставить точку

names.append("Polina")
names.append("Serega")
names.append("Simothy")
print(names)
names.remove("Polina")
print(names)

# print([1, 2, 3] + [4, 5, 6])
names.append("Polina")
names.append("Serega")
names.append("Simothy")
print(names)
# У каждого эдемента списка есть свой номер- называется индекс
# ИНДЕКСЫ НАЧИНАЮТСЯ С НУЛЯ!!!!!
# К элементу списка можно обратиться по его индексу
print(f"Привет {names[1]}")

sergey: str = names[0]

# ЧТОБЫ НАЙТИ КОЛЛИЧЕСТВО ЭЛЕМЕНТОВ В КОЛЛЕКЦИИ НУЖНО ИСПОЛЬЗОВАТЬ ФУНКЦИЮ len
print(len(names))
# Последний индекс в list будет равен len-1
print(names[len(names)-1])


# functions: list = [abs, sqrt, log2, factorial]
# for function in functions:
#     print(function(123))
