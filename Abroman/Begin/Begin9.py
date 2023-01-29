import math

first: float = float(input("Введите положительное значение а: "))
second: float = float(input("Введите положительное значение b: "))

# composition:float = first*second
mean: float = math.sqrt(first * second)

print(f"Среднее геометрическое с числами {first} и {second} равен: {mean}")
