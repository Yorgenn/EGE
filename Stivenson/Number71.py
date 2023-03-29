pi: float = 3.0
sign: int = 1
i: int = 2
while i <= 300000:
    pi = pi + 4 / (i * (i + 1) * (i + 2)) * sign

    sign *= (-1)
    i += 2

print(pi)
