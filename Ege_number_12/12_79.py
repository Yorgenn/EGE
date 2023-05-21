import random
from math import sqrt


def proc(s: str) -> str:
    while "25" in s or "355" in s or "555" in s:
        if "25" in s:
            s = s.replace("25", "3", 1)

        if "355" in s:
            s = s.replace("355", "52", 1)

        if "555" in s:
            s = s.replace("555", "23", 1)
    return s


def summ_str(s: str) -> int:
    sum_: int = 0
    for c in s:
        sum_ += int(c)
    return sum_


for n in range(4, 1000):
    s = "3" + "5" * n
    # print(n, proc(s), summ_str(proc(s)))
    if sum(map(int, proc(s))) == 27:
        print(n)
