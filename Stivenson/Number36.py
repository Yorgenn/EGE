human_age: float = float(input("Введите сколько лет прошло: "))

dog_age: float = 0
if int(human_age) == 1 or human_age == 2:
    dog_age = 10.5 * human_age
elif human_age > 2:
    dog_age = 21 + (human_age-2) * 4
else:
    print("Вы ввели неверное число:")

print(f"Возраст собаки равен: {dog_age} при {human_age} введных годах")
