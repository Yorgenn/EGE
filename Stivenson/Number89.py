def int_to_word(n: int) -> str:
    if n == 1:
        return "first"
    elif n == 2:
        return "second"
    elif n == 3:
        return "third"
    elif n == 4:
        return "fourth"
    elif n == 5:
        return "fifth"
    elif n == 6:
        return "sixth"
    elif n == 7:
        return "seventh"
    elif n == 8:
        return "eighth"
    elif n == 9:
        return "ninth"
    elif n == 10:
        return "tenth"
    elif n == 11:
        return "eleventh"
    elif n == 12:
        return "twelfth"
    else:
        return ""


i: int = 1
while i <= 12:
    print(f"I am the {int_to_word(i)} student.")
    i += 1
