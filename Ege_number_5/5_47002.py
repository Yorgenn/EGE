def algorithm(n: int) -> int:
    n_bin: str = bin(n)[2:]
    one_n: int = n_bin[1::2].count("1")
    zero_n: int = n_bin[0::2].count("0")
    return abs(zero_n - one_n)


for n in range(1, 10000):
    if algorithm(n) == 4:
        print(n)
