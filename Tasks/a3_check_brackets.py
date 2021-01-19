def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    if not brackets_row:
        return True
    a = 0
    for i in brackets_row:
        if i == "(":
            a += 1
        elif i == ")":
            a -= 1
        if a < 0:
            return False
    if a == 0:
        return True

if __name__ == "__main__":
    print(check_brackets(")()"))

