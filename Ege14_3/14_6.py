for x in "0123456789ABCDEFGHI":
    num1: int = int("321" + x + "4", 19)
    num2: int = int("498" + x + "9", 19)
    if (num1 + num2) % 23 == 0:
        print(x, (num1 + num2) // 23)
