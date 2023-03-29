from math import sqrt


def get_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_per(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3


def get_area(a: float, b: float, c: float) -> float:
    half_perimeter: float = get_per(a, b, c) / 2
    return sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))


x1: float = float(input("x1: "))
y1: float = float(input("y1: "))

x2: float = float(input("x2: "))
y2: float = float(input("y2: "))

x3: float = float(input("x3: "))
y3: float = float(input("y3: "))

a: float = get_distance(x1, y1, x2, y2)
b: float = get_distance(x2, y2, x3, y3)
c: float = get_distance(x1, y1, x3, y3)

per: float = get_per(a, b, c)
s: float = get_area(a, b, c)

print(f" Площадь треугольника равна: {s:.2f}\n Периметр равен: {per:.2f} ")
