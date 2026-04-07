def encrypt(word: str) -> str:
    new_word = ""
    vowels_value = {"a": 0, "e": 1, "i": 2, "o": 2, "u": 3}
    reverse_word = ""
    for ind in range(len(word) - 1, -1, -1):
        reverse_word = reverse_word + word[ind]
    for char in reverse_word:
        if char in vowels_value.keys():
            new_word = new_word + str(vowels_value[char])
        else:
            new_word += char
    return new_word + "aca"


print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))
print(encrypt("alpaca"))
