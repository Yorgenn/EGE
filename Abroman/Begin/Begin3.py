print("Ввидите длину:")
lenght: float = float(input())
print("Ввидите ширину :")
width: float = float(input())

s: float = lenght * width
p: float = 2 * (lenght + width)

print(f"Периметр прямоугольника со сторонами {lenght} и {width} равен {p}")
print(f"Площадь прямоугольника со сторонами {lenght} и {width} равен {s}")
