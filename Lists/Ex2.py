n: int = int(input("Введите количество имен: "))
names: list[str] = []

i = 1
while i <= n:
    names.append(input("Введите имя: "))
    i += 1

i = 0
while i < len(names):
    print(f"Hello {names[i]}")
    i += 1
