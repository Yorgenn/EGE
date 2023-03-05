#1 1 2 3 5 8 13 21 ..

def fib(n: int):
    print("!")
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n -1)


print(fib(100))
2**(2**(2**(65536)))