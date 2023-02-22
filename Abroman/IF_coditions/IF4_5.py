a: int = int(input("Введите число a: "))
b: int = int(input("Введите число b: "))
c: int = int(input("Введите число c: "))

positives: int = 0
negatives: int = 0
zeroes: int = 0

if a > 0:
    positives = positives + 1
elif a < 0:
    negatives = negatives + 1
else:
    zeroes = zeroes + 1

if b > 0:
    positives = positives + 1
elif b < 0:
    negatives = negatives + 1
else:
    zeroes = zeroes + 1

if c > 0:
    positives = positives + 1
elif c < 0:
    negatives = negatives + 1
else:
    zeroes = zeroes + 1

print(positives, negatives, zeroes)
print("конец программы")