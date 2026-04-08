def censor_string(text: str, words_list: list, char: str) -> str:
    new_text = ""
    text_split = text.split(" ")
    for word in text_split:
        if word in words_list:
            new_word = word.replace(word, char * len(word))
            new_text += new_word + " "
        else:
            new_text += word + " "
    return new_text.strip()


print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(
    censor_string(
        "Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"
    )
)
