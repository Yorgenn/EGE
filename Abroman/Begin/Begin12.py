import math

first: float = float(input("Введите положительное значение а: "))
second: float = float(input("Введите положительное значение b: "))

c: float = math.sqrt(first ** 2 + second ** 2)
p: float = first + second + c

print(f"Гипотенуза: {c}")
print(f"Периметр: {p}")