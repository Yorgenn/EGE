# будет считать факториал через цикл
def factoial(n: int) -> int:
    prod = 1
    for i in range(1, n + 1):
        prod = prod * i
    return prod


for i in range(16):
    print(f"{i}! = {factoial(i)}")
