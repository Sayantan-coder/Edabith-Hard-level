def prulaize(words_list: list) -> set:
    words_set = set()
    words = {}
    for word in words_list:
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1
    for word_ in words:
        if words[word_] > 1:
            word_ += "s"
            words_set.add(word_)
        else:
            words_set.add(word_)
    return words_set


print(prulaize(["cow", "pig", "cow", "cow"]))
print(prulaize(["table", "table", "table"]))
print(prulaize(["chair", "pencil", "arm"]))
