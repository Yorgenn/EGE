PI = 3.14

r1: float = float(input("Ввидите больший R1: "))
r2: float = float(input("Ввидите R2: "))

s1: float = PI * (r1 ** 2)
s2: float = PI * (r2 ** 2)
sRing: float = s1 - s2

print(f"При значениях {r1} и {r2},площадь большего круга равна {s1}, меньшего равна {s2}, а площадь кольца равна {sRing}")
