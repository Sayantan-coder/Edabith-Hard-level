def flip_bits(number: int) -> int:
    binary_str = ""

    def decimal_to_binary(num):
        nonlocal binary_str
        binary_str = ""
        while num:
            bit = num % 2
            binary_str = str(bit) + binary_str
            num = num // 2
        return binary_str

    decimal_to_binary(number)

    binary = ""
    flip_binary_version = ""
    length = len(binary_str)
    if length == 32:
        binary = binary_str
    else:
        binary_str = (32 - length) * "0" + binary_str
        binary = binary_str
    for bit in binary:
        if bit == "0":
            bit = "1"
            flip_binary_version += bit
        else:
            bit = "0"
            flip_binary_version += bit

    def binary_to_decimal(binary: str):
        decimal = 0
        for bit in binary:
            decimal = decimal * 2 + int(bit)
        return decimal

    return binary_to_decimal(flip_binary_version)


print(flip_bits(20))
print(flip_bits(15))
print(flip_bits(1))
print(flip_bits(4))
