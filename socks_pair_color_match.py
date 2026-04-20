def socks_pair(socks_list: list) -> int:
    if len(socks_list) == 0:
        return 0

    socks_frequency = {}
    for sock in socks_list:
        if sock in socks_frequency:
            socks_frequency[sock] = socks_frequency[sock] + 1
        else:
            socks_frequency[sock] = 1
    pair = 0
    for count in socks_frequency.values():
        pair = pair + (count // 2)
    return pair


print(socks_pair([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(socks_pair([50, 20, 30, 90, 30, 20, 50, 20, 90]))
print(socks_pair([]))
