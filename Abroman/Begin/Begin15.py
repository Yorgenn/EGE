import math

s: float = float(input("Ввидите площадь: "))

R: float = math.sqrt(s / 3.14)
L: float = 2 * 3.14 * R

print(f"При площади круга {s}, радиус равен {R}, а длина окружности равна {L}")