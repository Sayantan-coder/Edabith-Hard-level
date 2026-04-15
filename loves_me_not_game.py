def loves_me(n):
    result = ""
    i = 1

    while i <= n:

        if i % 2 == 1:
            phrase = "Loves me"
        else:
            phrase = "Loves me not"
        if i == n:
            upper_phrase = phrase.upper()
            result = result + upper_phrase
        else:
            result = result + phrase + "," + " "
        i = i + 1
    return result


print(loves_me(3))
print(loves_me(7))
print(loves_me(1))
