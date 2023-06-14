chars: str = "ABCDEX"

i: int = 0
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                word: str = c1 + c2 + c3 + c4
                if word.count("X") == 1:
                    i+=1
                    print(i, word)
