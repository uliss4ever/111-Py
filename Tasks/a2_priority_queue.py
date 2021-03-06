"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


priority_queue = [(9, 0), (3, 0), (8, 0), (5, 0), (6, 1)]
def enqueue(elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        if not priority_queue:
            priority_queue.append((elem, priority))
            return None
        else:
            i = 0
            while i < len(priority_queue) and priority_queue[i][1] <= priority:
                i += 1
            priority_queue.insert(i, (elem, priority))
        return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(priority_queue):
        t = priority_queue[0]
        del priority_queue[0]
        return t[0]

def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if not priority_queue:
        return None
    else:
        i = 0
        while ind < len(priority_queue) and priority_queue[i][1] <= priority and i < ind:
            i += 1
        if ind == i:
            return priority_queue[i][0]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_queue
    priority_queue.clear()
    return None
