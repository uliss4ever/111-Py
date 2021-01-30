"""
My little Queue
"""
from typing import Any

my_queue = []
def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_queue.insert(0, elem)
    print(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if len(my_queue):
        t = my_queue[-1]
        del my_queue[-1]
        return t
    return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if 0 <= ind < len(my_queue):
        return my_queue[-ind-1]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global my_queue
    my_queue.clear()
    return None
