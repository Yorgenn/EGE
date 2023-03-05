a: int = int(input("Введите число a: "))
b: int = int(input("Введите число b: "))

# if a > b:
# a, b = b, a

if a > b:
    temp = a
    a = b
    b = temp

print(f"Число a: {a}; Число b : {b}")
