# вывести факториалы первых 15 чисел

def get_factorial(n: int) -> int:
    i = 1
    prod: int = 1
    while i <= n:
        prod = i * prod

        i += 1
    return prod


n: int = 1
while n <= 100000:
    print(f"{n}- {get_factorial(n)}")

    n += 1
