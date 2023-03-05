a: int = int(input("Введите число a: "))
b: int = int(input("Введите число b: "))

raznost = a - b
n = 1
while raznost >= b:
    raznost -= b
    n += 1

print(f"Вместилось отрезков b на отрезке а:{n}; Остаток: {raznost}")
