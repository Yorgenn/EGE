def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for n in range(2, 105):
    if is_prime(n):
        print(n)
