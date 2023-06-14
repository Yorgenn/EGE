def ten_to_R(n: int, base: int) -> str:
    result: str = ""
    while n != 0:
        result += str(n % base)
        n = n // base
    return result[::-1]


print(ten_to_R(125 + 25 ** 3 + 5 ** 9, 5).count("0"))
