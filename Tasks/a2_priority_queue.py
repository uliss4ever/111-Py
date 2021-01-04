"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

priority_queue = []
def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    priority_queue.insert(0, (elem, priority))
    priority_queue.sort(key=lambda x: x[1], reverse=True)
    return None
print(enqueue(1, 0))

def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(priority_queue):
        t = priority_queue[-1]
        del priority_queue[-1]
        return t[0]
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    l = [i[0] for i in priority_queue if i[1] == priority]
    if 0 <= ind < len(l):
        return l[-ind -1]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_queue
    priority_queue.clear()
    return None
