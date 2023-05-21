def algorithm(n: int) -> int:
    n_bin: str = bin(n)[2:]
    # print(n_bin)
    result_srt: str = ""
    for c in n_bin:
        if c == "0":
            result_srt += "1"
        else:
            result_srt += "0"
    # print(result_srt)
    return n - int(result_srt, base=2)


for i in range(1, 10000):
    if algorithm(i) == 999:
        print(i)

