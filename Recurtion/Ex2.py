# напсиать функцию которая считает натуральную степень действительного числа РЕКУРСИВНО
def recursion_power(a: float, n: int) -> float:
    if n > 0:
        return a * recursion_power(a, n - 1)
    else:
        return 1


print(recursion_power(2, 1))
