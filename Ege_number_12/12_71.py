def proc(s: str) -> str:
    while "1111" in s:
        s = s.replace("1111", "22", 1)
        s = s.replace("222", "1", 1)
    return s


for n in range(200, 1001):
    s = "1" * n
    print(n, proc(s))
