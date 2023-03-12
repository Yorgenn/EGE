A: int = int(input("Введите число А: "))
B: int = int(input("Введите число B: "))

A_stock: int = A
B_stock: int = B

if A != B:
    A = B = max(A, B)
else:
    A = B = 0
print(f"Переменные {A_stock} и {B_stock} = {A} и {B}")
