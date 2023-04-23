def f(n: int) -> int:
    if n == 1:
        return 0
    else:
        return f(n - 1) + n


def g(n: int) -> int:
    if n == 1:
        return 1
    else:
        return g(n - 1) * n


print(f(5)+g(5))
