for x in "012345678":
    for y in "012345678":
        num1: int = int("88" + x + "4" + y, 9)
        num2: int = int("7" + x + "44" + y, 11)
        if (num1 + num2) % 61 == 0:
            print(x, y, (num1 + num2) // 61)
