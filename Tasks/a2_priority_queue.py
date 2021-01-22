"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


priority_queue = [(9, 0), (3, 0), (8, 0), (5, 0), (6, 1)]
def enqueue(elem: Any, priority: int = 0) -> None:
        if not priority_queue:
            priority_queue.append((elem, priority))
            return None
        else:
            i = 0
            while priority_queue[i][1] <= priority:
                i += 1
            priority_queue.insert(i, (elem, priority))
        return priority_queue

print(enqueue(0, 1))


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(priority_queue):
        t = priority_queue[0]
        del priority_queue[0]
        return t[0]
# print(dequeue())

def peek(ind: int = 0, priority: int = 0) -> Any:
    if not priority_queue:
        return None
    else:
        i = 0
        while priority_queue[i][1] <= priority and i < ind:
            i += 1
        if i == ind:
            return priority_queue[i]


print(peek(0, 0))

def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_queue
    priority_queue.clear()
    return None
