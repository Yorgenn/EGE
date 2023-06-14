for x in "0123456789":
    num1: int = int("4C" + x + "4", 15)
    num2: int = int(x + "62A", 13)
    if (num1 + num2) % 121 == 0:
        print(x, (num1 + num2) // 121)
