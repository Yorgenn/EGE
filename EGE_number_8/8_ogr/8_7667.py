chars: str = "ЕГЭ"

i: int = 0
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                for c5 in chars:
                    if c1 == "Е" or c1 == "Э":
                        i += 1
                        print(i, c1 + c2 + c3 + c4 + c5)
