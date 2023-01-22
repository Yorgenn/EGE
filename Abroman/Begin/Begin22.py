name1: str = input("Введите имя 1: ")
name2: str = input("Введите имя 2: ")

tmp = name1
name1 = name2
name2 = tmp

print(name1)
print(name2)
