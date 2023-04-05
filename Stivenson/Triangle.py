height: int = int(input("Введите положительную высоту: "))
while height <= 2:
    height: int = int(input("Введите положительную высоту: "))

width: int = int(input("Введите положительную ширину: "))
while width <= 2:
    width: int = int(input("Введите положительную ширину: "))

print(f"Ширина: {width}\nВысота: {height}")

row: int = 1
while row <= height:
    col: int = 1
    while col <= width:
        if row ==1 or row == height:
            print("#", end="")
        elif col == 1 or col == width:
            print("#", end="")
        else:
            print(" ", end="")

        col += 1
    print()

    row += 1