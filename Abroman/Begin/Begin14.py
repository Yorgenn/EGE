PI = 3.14  # константа

length: float = float(input("Введите длину окружности: "))

radius: float = length / (2 * PI)
area: float = PI * radius ** 2

print(f"У окружности длиной {length} радиус будет равен {radius}, а площадь круга будет равна {area}.")
