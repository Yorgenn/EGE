a: int = int(input("Введите число а:"))
b: int = int(input("Введите число b:"))

a_is_bigger_2: bool = a > 2
b_is_smaller_or_equal_3: bool = b <= 3
bool4_result: bool = a_is_bigger_2 and b_is_smaller_or_equal_3

bool5_result: bool = a >= 0 or b < -2

print(f"{a}>2 и {b}<=3: Первое высказывание:{a_is_bigger_2}; Второе высказывание:{b_is_smaller_or_equal_3}; "
      f"Конъюнкция: {bool4_result} ")
print(f"{a}>=0 или {b}<-2; Дизъюнкция: {bool5_result}")
