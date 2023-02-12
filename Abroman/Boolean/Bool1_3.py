a: int = int(input("Введите целое число"))

a_is_positive: bool = a > 0
a_is_odd: bool = a % 2 == 1  # проверка на нечетность
a_is_even: bool = a % 2 == 0  #  проверка на четность

print(f"Ваше число {a} является положительным?:{a_is_positive}")
print(f"Ваше число {a} является нечетным?:{a_is_odd}")
print(f"Ваше число {a} является четным?:{a_is_even}")
