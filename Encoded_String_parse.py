def parse_code(encoded_str: str) -> dict:
    first_name = ""
    last_name = ""
    user_id = ""
    i = 0
    n = len(encoded_str)

    while i < n and encoded_str[i] != "0":
        first_name += encoded_str[i]
        i += 1

    while i < n and encoded_str[i] == "0":
        i += 1

    while i < n and encoded_str[i] != "0":
        last_name += encoded_str[i]
        i += 1

    while i < n and encoded_str[i] == "0":
        i += 1

    while i < n:
        user_id += encoded_str[i]
        i += 1

    return {"first_name": first_name, "last_name": last_name, "id": user_id}


print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))
