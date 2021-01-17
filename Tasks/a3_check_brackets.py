import stack as stack

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
    for i in brackets_row:
        if i == "(":
            a += 1
        elif i == ")":
            a -= 1
    if a != 0:
        return False
    return True

print(check_brackets("())()"))

# def check_brackets(brackets_row: str) -> bool:
#     if not brackets_row:
#         return True
#     if brackets_row[0] == ")" or brackets_row[-1] == "(":
#         return False
#     for i in brackets_row:
#         if i == "(":
#             stack.push("(")
#         elif i == ")":
#             f = stack.pop()
#         if f == None:
#             return False
#     if stack.pop() != None:
#         return False
#     return True
#
#
# print(check_brackets("()((("))
#
# def check_brackets(brackets_row: str) -> bool:
#     if not brackets_row:
#         return True
#     if brackets_row[0] == ")" or brackets_row[-1] == "(":
#         return False
#     my_stack = []
#     for i in brackets_row:
#         if i == "(":
#             my_stack.insert(0, "(")
#         if i == ")" and my_stack:
#             if my_stack[0] == "(":
#                 my_stack.pop()
#         elif i == ")" and not my_stack:
#             my_stack.insert(0, ")")
#
#     if my_stack:
#         return False
#     return True
#
# print(check_brackets("(())())"))
#
