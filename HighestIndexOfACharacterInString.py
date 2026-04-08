def get_highest_index(name: str) -> str:
    alphabet = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    Index1 = 0
    Index2 = 0
    if len(name) == 1:
        return alphabet[name[0].lower()]
    else:
        max_index = alphabet[name[0].lower()]
        max_rest_index = get_highest_index(name[1:])
        if max_index > max_rest_index:
            Index1 = max_index
        else:
            Index2 = max_rest_index
    if Index1:
        return f"{Index1}{name[0]}"
    else:
        return f"{Index2}{name[0]}"


print(get_highest_index("Mango"))
print(get_highest_index("Sayantan"))
print(get_highest_index("Debasish"))
print(get_highest_index("Oscar"))
