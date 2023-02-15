x: int = int(input("Введите число от 1 до 8: "))
y: int = int(input("Введите число от 1 до 8: "))

#is_black: bool = x % 2 == 0 and y % 2 == 0 or x % 2 == 1 and y % 2 == 1
is_black: bool =(x % 2 == 1) == (y % 2 == 1)
is_white: bool = not is_black

print(f"Ваши координаты: {x},{y}; попадают на белую клетку:{is_white}")
#TODO сделать через сумму
