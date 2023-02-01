number: int = int(input("Введите какое то двузначное число:"))

right: int = number % 10
left: int = number // 10

sum_digits: int = left + right
prodaction: int = left * right

reversed_number: int = right * 10 + left * 1

print(left)  # TODO: сделать красивый вывод
print(right)
print(sum_digits)
print(prodaction)
print(reversed_number)
