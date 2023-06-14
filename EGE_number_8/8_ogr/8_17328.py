chars: str = "ГЕРАСИМ"

i: int = 0
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                for c5 in chars:
                    for c6 in chars:
                        for c7 in chars:
                            word: str = c1 + c2 + c3 + c4 + c5 + c6 + c7
                            if len(set(word)) == len(
                                    word) and "ГР" not in word and "ГС" not in word and "ГМ" not in word and\
                                    "РГ" not in word and "РС" not in word and\
                                    "РМ" not in word and "СМ" not in word and "СР" not in word and "СГ" not in word and\
                                    "МГ" not in word and "МР" not in word and "МС" not in word and "ЕА" not in word and\
                                    "ЕИ" not in word and "ИА" not in word and "ИЕ" not in word and "АЕ" not in word and\
                                    "АИ" not in word:
                                i += 1
                                print(i, word)
