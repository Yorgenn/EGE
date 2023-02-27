a: int = int(input("Введите число a: "))
b: int = int(input("Введите число b: "))

if a > b:
    a, b = b, a

print(f"Число a: {a}; Число b : {b}")
