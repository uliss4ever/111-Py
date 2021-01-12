from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if not arr:
        return None
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r)//2
        guess = arr[mid]
        if guess == elem:
            while arr[mid-1] == elem:
                mid -= 1
            return mid
        if guess > elem:
            r = mid - 1
        else:
            l = mid + 1
    # print(elem, arr)
    return None
print(binary_search(2, [1, 1, 1, 2, 2, 2, 2, 2]))