def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    if not brackets_row:
        return True
    if brackets_row[0] == ")" or brackets_row[-1] == "(":
        return False

    a = 0
    while True:
        for i in brackets_row:
            if i == "(":
                a += 1
            elif i == ")":
                a -= 1
        print(a)
        if a < 0:
            return False
        return True


print(check_brackets(""))


