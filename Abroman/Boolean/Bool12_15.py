a: int = int(input("Введите число а:"))
b: int = int(input("Введите число b:"))
c: int = int(input("Введите число c:"))

a_pozitive: bool = a > 0
b_pozitive: bool = b > 0
c_pozitive: bool = c > 0
all_pozitive: bool = a_pozitive and b_pozitive and c_pozitive
позитивчик: bool = a_pozitive > 0 or b_pozitive > 0 or c_pozitive
ровно_одно: bool = (a_pozitive > 0 and b_pozitive < 0 and c_pozitive < 0) or \
                   (b_pozitive>0 and a_pozitive<0 and c_pozitive<0) or \
                   (c_pozitive>0 and a_pozitive<0 and b_pozitive<0)\

ровно_два: bool = (a_pozitive > 0 and b_pozitive > 0 and c_pozitive < 0) or \
                   (b_pozitive>0 and a_pozitive<0 and c_pozitive>0) or \
                   (c_pozitive>0 and a_pozitive>0 and b_pozitive<0)

print(f" Число {a} положительно: {a_pozitive}; число {b} положительно: {b_pozitive};"
      f" Число {c} положительно: {c_pozitive}; Все числа положительные: {all_pozitive} ")
