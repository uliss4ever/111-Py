from typing import List
import time
from decimal import Decimal


def time_func(f):
    def inner(*ar, **kwa):
        m = 0
        for a in range(100):
            t = time.time()
            res = f(*ar, **kwa)
            t1 = time.time()-t
            m += t1
        print(round(Decimal(m/100), 7))
        return m
    return inner


@time_func

def part(numms, left, right):
    mid = numms[(left + right)//2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while numms[i] < mid:
            i += 1
        j -= 1
        while numms[j] > mid:
            j -= 1
        if i >= j:
            return j
        temp = numms[i]
        numms[i] = numms[j]
        numms[j] = temp


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def _sort(items, left, right):
        if left < right:
            t = part(items, left, right)
            _sort(items, left, t)
            _sort(items, t + 1, right)
    _sort(container, 0, len(container)-1)
    return container
l = [1, 4, 6, 8, 3, 2, 0]
print(sort(l))