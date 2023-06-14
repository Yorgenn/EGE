chars: str = "МЕТРО"

i: int = 0
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                if (c1 == "М" or c1 == "Т" or c1 == "Р") and (c4 == "Е" or c4 == "О"):
                    i += 1
                    print(i, c1 + c2 + c3 + c4)
