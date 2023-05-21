def algorithm(n: int) -> int:
    bin_n: str = bin(n)[2:]
    if n % 3 == 0:
        bin_n = bin_n + bin_n[-3:]
    else:
        bin_n += bin((n % 3) * 3)[2:]

    return int(bin_n, base=2)


for n in range(1, 1000):
    if algorithm(n) > 76:
        print(n)


print(algorithm(11))