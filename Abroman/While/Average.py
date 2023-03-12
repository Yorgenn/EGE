number: str = input("Введите чсило: ")
sum_: float = 0
i: int = 0
while number != '':
    sum_ += float(number)
    i += 1

    number = input("Введите чсило: ")

if i == 0:
    average: float = 0
else:
    average: float = sum_ / i

print(f"Average: {average} ")
