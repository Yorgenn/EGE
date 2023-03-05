a: int = int(input("Введите число а: "))
b: int = int(input("Введите число b: "))

if a != b:
    a, b = a + b, a + b
else:
    a = b = 0

print(a, b)
