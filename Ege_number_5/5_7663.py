def algorithm(n: int) -> int:
    n_str: str = str(n)
    part_1: int = int(n_str[0]) + int(n_str[1])
    part_2: int = int(n_str[1]) + int(n_str[2])
    if part_1 > part_2:
        return int(str(part_1) + str(part_2))
    else:
        return int(str(part_2) + str(part_1))



for n in range(100, 1000):
    if algorithm(n) == 1412:
        print(n)
