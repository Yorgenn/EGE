x: int = int(input("Введите число: "))  # Третья форма условного оператора(Elif)

if x > 0:
    x = x + 1
elif x < 0:
    x = x - 2
# elif x < 0:
#     x = x - 2
# elif x < 0:
#     x = x - 2
else:
    x = 10

print(x)
print("Конец программы")
