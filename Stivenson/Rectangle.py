height: int = int(input("Введите положительную высоту: "))
while height <= 0:
    height: int = int(input("Введите положительную высоту: "))

width: int = int(input("Введите положительную ширину: "))
while width <= 0:
    width: int = int(input("Введите положительную ширину: "))

print(f"Ширина: {width}\nВысота: {height}")

# 3x6
# ******
# ******
# ******
row: int = 1
while row <= height:
    col: int = 1
    while col <= width:
        print("*", end="")

        col += 1
    print()

    row += 1
