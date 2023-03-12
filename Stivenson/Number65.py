MIN: float = 0.0
MAX: float = 100.0
STEP: float = 10.0

celsius: float = MIN
while celsius <= MAX:
    fahrenheit: float = celsius * (9/5) + 32
    print(f"|{celsius:^15.3f}|{fahrenheit:^15.3f}|")

    celsius += STEP

