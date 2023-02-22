number: int = int(input("Введите какое то трехзначное число:"))

left = number // 100
mid = (number - left * 100) // 10
right = number % 10

print(f"Сотни: {left}; Десятки: {mid};Единицы: {right}; Сумма этих чисел равна:{left + mid + right}, "
      f"а произведение:{left * mid * right}.")

reversed_number: int =
print(f"Число при прочтении справа налево будет выглядить как {right}{mid}{left}.")
print(f"При переносе соток в еденицы число будет выглядить так:{mid}{right}{left}")
print(f"При переносе едениц в сотки число будет выглядить так:{right}{left}{mid}")
print(f"При переносе соток с десятками число будет выглядить так:{mid}{left}{right}")
print(f"При перестановке десятков и едениц число будет выглядить так:{left}{right}{mid}")
#TODO переделать