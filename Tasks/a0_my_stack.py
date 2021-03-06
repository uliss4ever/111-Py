"""
My little Stack
"""
from typing import Any

my_stack = []
def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    my_stack.insert(0, elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if len(my_stack):
        return my_stack.pop(0)

def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    if 0 <= ind < len(my_stack):
        return my_stack[ind]
    return None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global my_stack
    my_stack.clear()
    return None
