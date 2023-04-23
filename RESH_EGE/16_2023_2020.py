import sys
from functools import lru_cache


print(sys.setrecursionlimit(20000))


@lru_cache(maxsize=20000)
def f(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * f(n - 1)


print(f(2023) / f(2020))
