from typing import List

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
# l = [6, 8, 23, 4, 1, 90, 84, 56]
# print(sort(l))