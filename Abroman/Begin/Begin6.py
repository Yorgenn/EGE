lenght1: float = float(input("Ввидите длину ребра а: "))
lenght2: float = float(input("Ввидите длину ребра b: "))
lenght3: float = float(input("Ввидите длину ребра с: "))

v: float = lenght1 * lenght2 * lenght3
s: float = 2 * (lenght1 * lenght2 + lenght2 * lenght3 + lenght1 * lenght3)

print(f"Объем прямоугольного параллепипида со сторонами {lenght1}, {lenght2} и {lenght3} равен {v}")
print(f"Площадь поверхности прямоугольного параллепипида со сторонами {lenght1}, {lenght2} и {lenght3} равен {s}")