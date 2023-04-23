def is_triangle(side1: int, side2: int, side3: int) -> bool:
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
    elif side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False


a: int = int(input("Введите длину a: "))
b: int = int(input("Введите длину b: "))
c: int = int(input("Введите длину c: "))

if is_triangle(a, b, c):
    print("Такой треугольник возможен.")
else:
    print(f"Треугольник со сторонами {a}, {b}, {c}- невозможен.")