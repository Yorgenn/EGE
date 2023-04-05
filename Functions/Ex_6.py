def convert_to_bin(n: int) -> str:
    s: str = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


a: int = int(input("Введите число: "))
i: int = 1
while i <= a:
    print(f"Исходное число: {i}; В двоичной системе: {convert_to_bin(i)} ")
    i += 1
