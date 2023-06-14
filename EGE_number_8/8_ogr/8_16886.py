chars: str = "МАТВЕЙ"

i: int = 0
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                for c5 in chars:
                    for c6 in chars:
                        word: str = c1 + c2 + c3 + c4 + c5 + c6
                        if c1 != "Й" and word.count("АЕ") == 0 and word.count("А") == 1 and word.count(
                                "М") == 1 and word.count("Т") == 1 and word.count("В") == 1 and word.count(
                                "Е") == 1 and word.count("Й") == 1:
                            i += 1
                            print(i, word)
