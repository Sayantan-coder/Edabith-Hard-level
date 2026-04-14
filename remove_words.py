def remove_letters(char_list: list, word: str) -> list:
    words_list = {}
    for char in word:
        if char in words_list:
            words_list[char] = words_list[char] + 1
        else:
            words_list[char] = 1
    new_list = []
    for char in char_list:
        if char in words_list and words_list[char] > 0:
            words_list[char] -= 1
        else:
            new_list.append(char)
    return new_list


print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))
