for a in range(1, 10000):
    for x in "012345678":
        M: int = int("842" + x + "5", 9)
        N: int = int("8" + x + "725", 9)
        if (M + a) % N == 0:
            print(a)
