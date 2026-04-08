def change_format_hyperlink(url: str, name: str, hover_text: str = None):
    if hover_text:
        return f'[{name}]({url} "{hover_text}")'
    else:
        return f"[{name}]({url})"


print(
    change_format_hyperlink(
        "https://edabit.com/challenges", "this", "Go to the challenges!"
    )
)
print(change_format_hyperlink("https://www.google.com", "Google", "Google Search"))
print(
    change_format_hyperlink("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!")
)
