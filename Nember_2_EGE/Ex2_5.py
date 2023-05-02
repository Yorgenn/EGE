def implication(a: bool, b: bool) -> bool:
    return not a or b


print("x y z w")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not ((implication(x, y) and implication(y, w)) or (z == (x or y))):
                    print(x, y, z, w)
