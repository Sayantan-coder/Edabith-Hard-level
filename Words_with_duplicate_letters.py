def check_duplicate_letters(text: str) -> bool:
    words_list = []
    i = 0
    n = len(text)
    while i < n:
        while i < n and text[i] == " ":
            i += 1
        start = i
        while i < n and text[i] != " ":
            i += 1
        if i < n:
            word = text[start:i]
            words_list.append(word)

    for word in words_list:
        temp_word = ""
        for ch in word:
            if ch not in temp_word:
                temp_word += ch
            else:
                return False
    return True


print(
    check_duplicate_letters(
        "You can lead a horse to water, but you can't make him drink."
    )
)
print(check_duplicate_letters("Look before you leap."))
print(check_duplicate_letters("An apple a day keeps the doctor away."))
print(check_duplicate_letters("Fortune favours the bold."))
