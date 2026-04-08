def convert_to_hex(text: str) -> str:
    hex_list = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
    }
    ASCII_Code_list = [ord(char) for char in text]

    def ascii_code_to_hex(Code_list: list):
        result = ""
        for code in Code_list:
            if code == 0:
                result += "0"
                continue

            new_text = ""
            while code:
                remainder = code % 16
                new_text = hex_list[remainder] + new_text
                code = code // 16
            result = result + new_text + " "
        return result.strip()

    return ascii_code_to_hex(ASCII_Code_list)


print(convert_to_hex("hello world"))
print(convert_to_hex("Big Boi"))
print(convert_to_hex("Marty Poppinson"))
print(convert_to_hex("Sayantan Banerjee"))
