FIRST_PRICE: float = 10.95
OTHER_PRICE: float = 2.95


def get_order_price(n: int) -> float:
    return FIRST_PRICE + (OTHER_PRICE * (n - 1))


goods: int = int(input("Введите количество товаров: "))
price: float = get_order_price(goods)

print(f"Количество позиций в вашем заказе={goods}, стоимость доставки={price:.2f}")
