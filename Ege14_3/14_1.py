for x in "0123456789ABCDE":
    num1: int = int("123" + x + "5", 15)
    num2: int = int("1" + x + "233", 15)
    # print(num1, num2)
    if (num1 + num2) % 14 == 0:
        print(x, (num1 + num2) // 14)
