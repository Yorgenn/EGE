from math import sqrt


def get_hypot(a: float, b: float) -> float:
    return sqrt(a ** 2 + b ** 2)


side1: float = float(input("Введите длину 1 катита:"))
side2: float = float(input("Введите длину 2 катита:"))

hypot: float = get_hypot(side1, side2)

print(f"Гипатенуза треугольника равна: {hypot:.2f}")
