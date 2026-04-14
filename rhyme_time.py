def does_rhyme(text1: str, text2: str) -> bool:
    text1_words_list = []
    text2_words_list = []
    i1 = 0
    i2 = 0
    n1 = len(text1)
    n2 = len(text2)
    while i1 < n1:
        while i1 < n1 and text1[i1] == " ":
            i1 += 1
        start = i1
        while i1 < n1 and text1[i1] != " ":
            i1 += 1
        if start < n1:
            word = text1[start:i1]
            text1_words_list.append(word)
    while i2 < n2:
        while i2 < n2 and text2[i2] == " ":
            i2 += 1
        start = i2
        while i2 < n2 and text2[i2] != " ":
            i2 += 1
        if start < n2:
            word = text2[start:i2]
            text2_words_list.append(word)
    vowels_list = ["a", "e", "i", "o", "u"]
    store1 = ""
    store2 = ""
    for ch in text1_words_list[len(text1_words_list) - 1]:
        if ch.lower() in vowels_list:
            store1 += ch.lower()
    for ch in text2_words_list[len(text2_words_list) - 1]:
        if ch.lower() in vowels_list:
            store2 += ch.lower()
    if store1 == store2:
        return True
    else:
        return False


print(does_rhyme("Sam I am!", "Green eggs and ham."))
print(does_rhyme("Sam I am!", "Green eggs and HAM."))
print(does_rhyme("You are off to the races", "a splendid day."))
print(does_rhyme("and frequently do?", "you gotta move."))
