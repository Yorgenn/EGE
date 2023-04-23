def f(n: int) -> int:
    if n == 1:
        return 1
    else:
        return f(n - 1) * f(n - 1) - f(n - 1) * n + 2 * n


print(f(4))
