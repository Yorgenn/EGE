chars: list[str] = ["А", "О", "У"]

i: int = 0
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                for c5 in chars:
                    i += 1
                    if f"{c1}{c2}{c3}{c4}{c5}" == "ОАОАО":
                        print(i)
