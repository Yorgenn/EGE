import math

corner: float = input("Введите значение угла a (0<a<2Пи)  :")

radian = math.pi * corner
degree = radian * 180 / math.pi

print(f"Радиана равна:{radian}; Значение угла в градусах равно:{degree}")
