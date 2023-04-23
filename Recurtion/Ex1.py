# Создать функцию вычисляющую факториал натурального числа РЕКУРСИВНО

def recursion_factorial(n: int) -> int:
    if n > 0:
        return recursion_factorial(n - 1) * n  # нисходящая рекурсия
        # return n * recursion_factorial(n - 1) #восходящая рекурсия(хвостовая рекурсия)
    else:
        return 1


print(recursion_factorial(5))


factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))
