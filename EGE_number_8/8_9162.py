chars: list[str] = ["М", "С", "Т", "Ф"]

i: int = 0
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                i += 1
                if i == 138:
                    print(c1, c2, c3, c4)
