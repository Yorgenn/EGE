first: float = float(input("Введите  значение а: "))
second: float = float(input("Введите  значение b: "))

First2: float = first ** 2
Second2: float = second ** 2

print(f"Сумма  равна: {First2 + Second2}; разность равна:{First2 - Second2}; Произведение равно: {First2 * Second2};"
      f" Частное равно: {First2 / Second2} при значениях {First2} и {Second2}.")
