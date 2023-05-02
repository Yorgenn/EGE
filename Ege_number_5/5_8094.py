def algoritm(n: int) -> int:
    n_bin: str = bin(n)[2:]
    # print(n_bin)#TODO написать функцию подсчета суммы цифор числа
    n_bin = n_bin + str(n_bin.count("1") % 2)
    # print(n_bin)
    n_bin = n_bin + str(n_bin.count("1") % 2)
    # print(n_bin)
    return int(n_bin, base=2)



for i in range(1, 100):
    print(i, algoritm(i))
