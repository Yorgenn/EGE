a: int = int(input("Введите любое число: "))
a_stock = a

while a >= 3:
    a /= 3

print(f"Число {a_stock} является степенью 3: ", (a == True))
