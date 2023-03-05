def factorial(n: int):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


f = factorial(700)
print(f)
input()
print(f)