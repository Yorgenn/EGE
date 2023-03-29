BASIC_TARIF: float = 4.0
BONUS_PRICE: float = 0.25


def calculate_price(m: int) -> float:
    return BASIC_TARIF + (BONUS_PRICE * (m // 140))


km: float = float(input("Введите сколько вы проехали километров: "))
m: int = int(km * 1000)
price:float = calculate_price(m)

print(f"Общая плата за поездку состовляет: {price:.2f}$")
