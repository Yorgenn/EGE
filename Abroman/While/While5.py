a: int = int(input("Введите число а: "))
b: int = 2 ** a
b_stock: int = b

a_new: int = 0
while b >= 2:
    b /= 2
    a_new += 1
print(f"Показатель этой степени = {a_new}, a 2ка в этой степени будет равна: {b_stock}")
