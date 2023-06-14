def ten_to_third(n: int) -> str:
    result: str = ""
    while n != 0:
        result += str(n % 3)
        n = n // 3
    return result[::-1]


print(ten_to_third(9**8+3**5-9).count("2"))
