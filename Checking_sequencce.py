def seq_level(*seq) -> str:
    seq_list = list(seq)
    current = seq_list[:]
    level = 0
    while level <= 3:
        is_consistent = True
        first_element = current[0]
        for num in current:
            if num != first_element:
                is_consistent = False
                break
        if is_consistent and len(current) >= 2:
            if level == 1:
                return "Linear"
            elif level == 2:
                return "Quadratic"
            else:
                return "Cubic"
        next_difference = []
        for ind in range(len(current) - 1):
            value = current[ind + 1] - current[ind]
            next_difference.append(value)
        current = next_difference
        level = level + 1


print(seq_level(1, 2, 3, 4, 5))
print(seq_level(3, 6, 10, 15, 21))
print(seq_level(4, 14, 40, 88, 164))
