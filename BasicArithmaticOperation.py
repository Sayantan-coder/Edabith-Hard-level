def arithmatic_operation(expr: str) -> int:
    expr_list = expr.split(" ")
    if expr_list[1] == "//":
        if int(expr_list[2]) == 0:
            return -1
        else:
            return int(expr_list[0]) // int(expr_list[2])
    elif expr_list[1] == "+":
        return int(expr_list[0]) + int(expr_list[2])
    elif expr_list[1] == "*":
        return int(expr_list[0]) * int(expr_list[2])
    else:
        return int(expr_list[0]) - int(expr_list[2])


print(arithmatic_operation("12 + 12"))
print(arithmatic_operation("12 - 12"))
print(arithmatic_operation("12 * 12"))
print(arithmatic_operation("12 // 0"))
