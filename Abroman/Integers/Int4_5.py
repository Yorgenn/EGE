a: int = int(input("Введите число:"))
b: int = int(input("Введите число меньше первого:"))

print(f"На отрезке длиною {a}см, помещается {a // b} отрезка длинной {b}см, остается {a % b}см.")