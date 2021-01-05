def check_brackets(brackets_row: str) -> bool:
    if not brackets_row:
        return True
    if brackets_row[0] == ")" or brackets_row[-1] == "(":
        return False
    my_stack = []
    for i in brackets_row:
        if i == "(":
            my_stack.insert(0, "(")
        if i == ")" and my_stack:
            if my_stack[0] == "(":
                my_stack.pop()
        elif i == ")" and not my_stack:
            my_stack.insert(0, ")")

    if my_stack:
        return False
    return True