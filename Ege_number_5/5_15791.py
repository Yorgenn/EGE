def algoritm(n: int) -> int:
    n_bin: str = bin(n)[2:]
    n_bin = n_bin + str(n_bin.count("1") % 2)
    n_bin = n_bin + str(n_bin.count("1") % 2)
    return int(n_bin, base=2)


for i in range(1, 1001):
    if algoritm(i) > 97:
        print(i, algoritm(i))
