a: int = int(input("Введите число: "))
n: int = int(input("Введите систему счисления от 2 до 9: "))

s = ''
curent_number:int = a
while curent_number > 0:
    s = str(curent_number % n) + s
    curent_number //= n

print(f"Число: {a} в {n} системе счисления равняется: {s}")
