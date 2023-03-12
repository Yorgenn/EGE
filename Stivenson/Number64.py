DISCOUNT: float = 0.60
MIN: float = 4.95
MAX: float = 24.95
STEP: float = 5.0

print(f"|Старая цена |Новая цена  |")
old_price: float = MIN
while old_price <= MAX:
    # new_price:float = old_price - DISCOUNT * old_price
    new_price: float = old_price * (1 - DISCOUNT)
    print(f"|{old_price:^12.2f}|{new_price:^12.2f}|")

    old_price += STEP
