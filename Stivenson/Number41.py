a: int = int(input("Введите сторону a: "))
b: int = int(input("Введите сторону b: "))
c: int = int(input("Введите сторону с: "))

if a == b and b == c:
    type_ = "равносторонний"
elif a == b or a == c or c == b:
    type_ = "равнобедренный"
else:
    type_ = "разносторонний"

print(f"Это {type_} треугольник👍")

