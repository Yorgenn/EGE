print("Ввидите длину ребра а:")
lenght1: float = float(input())
print("Ввидите длину ребра в:")
lenght2: float = float(input())
print("Ввидите длину ребра с:")
lenght3: float = float(input())


v: float = lenght1 * lenght2 * lenght3
s: float = 2 * (lenght1 * lenght2 + lenght2 * lenght3 + lenght1 * lenght3)

print(f"Объем прямоугольного параллепипида со сторонами {lenght1}, {lenght2} и {lenght3} равен {v}")
print(f"Площадь поверхности прямоугольного параллепипида со сторонами {lenght1}, {lenght2} и {lenght3} равен {s}")