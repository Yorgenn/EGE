sides: int = int(input("Введите количество сторон от 3 до 10: "))

if sides == 3:
    shape = "Треугольник"
elif sides == 4:
    shape = "Четырехугольник"
elif sides == 5:
    shape = "Пятиугольник"
elif sides == 6:
    shape = "Шестиугольник"
elif sides == 7:
    shape = "Семиугольник"
elif sides == 8:
    shape = "Восьмиугольник"
elif sides == 9:
    shape = "Девятиугольник"
elif sides == 10:
    shape = "Десятиугольник"
else:
    shape= "Ввели неверное число: Error "

print(shape)
