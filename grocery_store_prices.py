def get_prices(string_list: list) -> list:
    price_list = []
    i = 0
    while i < len(string_list):
        item = string_list[i]
        ind = 0
        price_str = ""
        while ind < len(item):
            char = item[ind]
            if ("0" <= char <= "9") or char == ".":
                price_str += char
            ind += 1
        price_number = float(price_str)
        price_list.append(price_number)
        i = i + 1
    return price_list


print(get_prices(["salad ($4.99)"]))
print(get_prices(["artichokes ($1.99)", "rotiserrie chicken ($5.99)", "gum ($0.75)"]))
print(
    get_prices(
        ["ice cream ($5.99)", "banana ($0.20)", "sandwich ($8.50)", "soup ($1.99)"]
    )
)
