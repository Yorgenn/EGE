first: float = float(input("Введите  значение а: "))
second: float = float(input("Введите значение b: "))

absFirst: float = abs(first)
absSecond: float = abs(second)

print(f"Сумма модулей равна: {absFirst + absSecond}; разность модулей равна:{absFirst - absSecond}; Произведение модулей равно: {absFirst * absSecond}; Частное модулей равно: {absFirst / absSecond}.")
