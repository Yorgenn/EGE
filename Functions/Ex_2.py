def greet_concret_user(
        name: str):  # name- это параметр функции их может быть несколько (эта информация нужная функции для работы)
    print(f"Hello {name}")


greet_concret_user("Yura")
greet_concret_user(input())
