s: str = "8" * 68
# оператор in определяет, принадлежит ли левый элемент, к коллекции справа (bool)
# print(1 in [1, 2, 3])
# print("world " in "hello world ")
while "222" in s or "888" in s:
    if "222" in s:
        s = s.replace("222", "8", 1)
    else:
        s = s.replace("888", "2", 1)


print(s)
