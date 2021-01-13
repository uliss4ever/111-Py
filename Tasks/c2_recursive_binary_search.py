from typing import Sequence, Optional


def help_req(elem: int, arr: Sequence, left, right):
    if not arr:
        return None
    while right >= left:
        mid = (left + right) // 2
        if arr[mid] == elem:
            while mid >= 1 and arr[mid - 1] == elem :
                mid -= 1
            return mid
        elif elem < arr[mid]:
            return help_req(elem, arr, left, mid - 1)
        elif elem > arr[mid]:
            return help_req(elem, arr, mid + 1, right)
    return None


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    return help_req(elem, arr, 0, len(arr))


print(binary_search(2, [2, 2, 2, 2, 2, 2, 2]))

