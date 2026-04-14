def vowels_link(text: str) -> bool:
    words_list = []
    i = 0
    n = len(text)
    while i < n:
        while i < n and text[i] == " ":
            i += 1
        start = i
        while i < n and text[i] != " ":
            i += 1
        if start < n:
            word = text[start:i]
            words_list.append(word)
    vowels_list = ["a", "e", "i", "o", "u"]
    for ind in range(len(words_list) - 1):
        if words_list[ind][-1] in vowels_list and words_list[ind + 1][0] in vowels_list:
            return True
    return False


print(vowels_link("go to edabit"))
print(vowels_link("an open fire"))
print(vowels_link("a sudden applause"))
print(vowels_link("a very large appliance"))
