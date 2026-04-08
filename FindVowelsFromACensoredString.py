def find_remove_vowels(text: str, word: str) -> str:
    result = ""
    for char in text:
        if char == "*":
            char = word[0]
            result += char
            word = word[1:]
        else:
            result += char
    return result


print(find_remove_vowels("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(find_remove_vowels("abcd", ""))
print(find_remove_vowels("*PP*RC*S*", "UEAE"))
